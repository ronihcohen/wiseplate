"""Upload a finished episode from out/<slug>/ to YouTube (stdlib only).

    python3 video/upload.py <episode> [--dry-run] [--privacy private|unlisted|public]

Reads YT_CLIENT_ID, YT_CLIENT_SECRET and YT_REFRESH_TOKEN from the
environment. Uploads <slug>.mp4 with the title, description and tags from
youtube.txt, then sets thumbnail.jpg and adds subtitles.en.srt as English
captions. Uploads are private unless --privacy says otherwise.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://www.googleapis.com/youtube/v3"
UPLOAD = "https://www.googleapis.com/upload/youtube/v3"
CHUNK = 8 * 1024 * 1024


def http(method, url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            body = r.read()
            return r, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        if e.code == 308:
            return e, {}
        raise SystemExit(f"HTTP {e.code} {method} {url.split('?')[0]}: {body[:800]}")


def access_token():
    data = urllib.parse.urlencode({
        "client_id": os.environ["YT_CLIENT_ID"],
        "client_secret": os.environ["YT_CLIENT_SECRET"],
        "refresh_token": os.environ["YT_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    }).encode()
    _, tok = http("POST", "https://oauth2.googleapis.com/token", data,
                  {"Content-Type": "application/x-www-form-urlencoded"})
    return tok["access_token"]


def parse_meta(path):
    """Title, description and tags from the sections of youtube.txt."""
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()

    def section(start, stops):
        out, on = [], False
        for ln in lines:
            if ln.startswith(start):
                on = True
                continue
            if on and any(ln.startswith(s) for s in stops):
                break
            if on:
                out.append(ln)
        return "\n".join(out).strip()

    title = section("TITLE", ["Shorter alternatives", "DESCRIPTION"]).splitlines()[0].strip()
    desc = section("DESCRIPTION", ["TAGS"])
    tags = [t.strip() for t in section("TAGS", ["CATEGORY"]).replace("\n", ",").split(",") if t.strip()]
    return title, desc, tags


def check(title, desc, tags):
    errs = []
    if not title or len(title) > 100:
        errs.append(f"title length {len(title)} (max 100)")
    if len(desc) > 5000:
        errs.append(f"description length {len(desc)} (max 5000)")
    if "<" in desc or ">" in desc:
        errs.append("description contains < or >")
    # YouTube counts quoted multi-word tags with their quotes plus separators.
    tag_len = sum(len(t) + (2 if " " in t else 0) for t in tags) + max(len(tags) - 1, 0)
    if tag_len > 500:
        errs.append(f"tags length {tag_len} (max 500)")
    return errs, tag_len


def upload_video(token, mp4, body):
    size = os.path.getsize(mp4)
    r, _ = http("POST", UPLOAD + "/videos?uploadType=resumable&part=snippet,status",
                json.dumps(body).encode(),
                {"Authorization": "Bearer " + token,
                 "Content-Type": "application/json; charset=UTF-8",
                 "X-Upload-Content-Type": "video/mp4",
                 "X-Upload-Content-Length": str(size)})
    loc = r.headers["Location"]
    sent = 0
    with open(mp4, "rb") as f:
        while sent < size:
            chunk = f.read(CHUNK)
            end = sent + len(chunk) - 1
            r, res = http("PUT", loc, chunk, {
                "Authorization": "Bearer " + token,
                "Content-Length": str(len(chunk)),
                "Content-Range": f"bytes {sent}-{end}/{size}"})
            sent = end + 1
            print(f"  {100 * sent // size}%", flush=True)
    return res


def find_by_title(token, title):
    _, res = http("GET", API + "/search?part=snippet&forMine=true&type=video&maxResults=10",
                  headers={"Authorization": "Bearer " + token})
    for item in res.get("items", []):
        if item["snippet"]["title"] == title:
            return item["id"]["videoId"]
    return None


def set_thumbnail(token, vid, jpg):
    http("POST", UPLOAD + "/thumbnails/set?videoId=" + vid, open(jpg, "rb").read(),
         {"Authorization": "Bearer " + token, "Content-Type": "image/jpeg"})


def add_captions(token, vid, srt):
    boundary = "wiseplate-caption-boundary"
    meta = {"snippet": {"videoId": vid, "language": "en", "name": "English"}}
    body = (f"--{boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n"
            f"{json.dumps(meta)}\r\n--{boundary}\r\nContent-Type: application/octet-stream\r\n\r\n"
            ).encode() + open(srt, "rb").read() + f"\r\n--{boundary}--\r\n".encode()
    http("POST", UPLOAD + "/captions?uploadType=multipart&part=snippet", body,
         {"Authorization": "Bearer " + token,
          "Content-Type": f"multipart/related; boundary={boundary}"})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("episode")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--privacy", default="private", choices=["private", "unlisted", "public"])
    a = ap.parse_args()
    slug = a.episode.replace("_", "-")
    out = os.path.join(HERE, "out", slug)
    files = {k: os.path.join(out, v) for k, v in {
        "mp4": slug + ".mp4", "thumb": "thumbnail.jpg",
        "srt": "subtitles.en.srt", "meta": "youtube.txt"}.items()}
    missing = [p for p in files.values() if not os.path.exists(p)]
    if missing:
        raise SystemExit("missing: " + ", ".join(missing))
    title, desc, tags = parse_meta(files["meta"])
    errs, tag_len = check(title, desc, tags)
    print(f"title ({len(title)}): {title}\ndescription: {len(desc)} chars, tags: {len(tags)} ({tag_len} chars)")
    if errs:
        raise SystemExit("youtube.txt problems: " + "; ".join(errs))
    if a.dry_run:
        print("dry run OK")
        return
    token = access_token()
    body = {"snippet": {"title": title, "description": desc, "tags": tags,
                        "categoryId": "27", "defaultLanguage": "en",
                        "defaultAudioLanguage": "en"},
            "status": {"privacyStatus": a.privacy, "selfDeclaredMadeForKids": False}}
    try:
        vid = upload_video(token, files["mp4"], body)["id"]
    except SystemExit as e:
        # The last chunk sometimes answers 410 Gone even though YouTube kept
        # the file, so look for the new video by title before giving up.
        print(f"upload reported: {e}")
        vid = find_by_title(token, title)
        if not vid:
            raise
    print(f"VIDEO {vid} https://studio.youtube.com/video/{vid}/edit")
    for name, fn, path in (("thumbnail", set_thumbnail, files["thumb"]),
                           ("captions", add_captions, files["srt"])):
        try:
            fn(token, vid, path)
            print(f"{name}: OK")
        except SystemExit as e:
            print(f"{name}: FAILED {e}")


if __name__ == "__main__":
    sys.exit(main())
