(() => {
  const root = document.querySelector('.site-search');
  if (!root) return;
  const input = root.querySelector('input');
  const panel = root.querySelector('.search-panel');
  const list = root.querySelector('[role="listbox"]');
  const status = root.querySelector('[role="status"]');
  let indexPromise;
  let results = [];
  let active = -1;
  let revision = 0;

  // Ignore case, punctuation and Hebrew vowel/cantillation marks.
  const normalize = (value) => value.normalize('NFKD').toLowerCase()
    .replace(/\p{M}/gu, '').replace(/[^\p{L}\p{N}]+/gu, ' ').trim();

  function close() {
    revision++;
    panel.hidden = true;
    input.setAttribute('aria-expanded', 'false');
    input.removeAttribute('aria-activedescendant');
    active = -1;
  }

  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch(root.dataset.searchIndex)
        .then((response) => {
          if (!response.ok) throw new Error('Search index unavailable');
          return response.json();
        })
        .then((pages) => pages.map((page) => ({
          ...page,
          name: normalize(page.title),
          text: normalize(page.terms.join(' ')),
        })))
        .catch((error) => {
          indexPromise = undefined; // Allow retry on the next interaction.
          throw error;
        });
    }
    return indexPromise;
  }

  async function search() {
    const current = ++revision;
    const query = normalize(input.value);
    results = [];
    active = -1;
    list.replaceChildren();
    input.removeAttribute('aria-activedescendant');
    input.setAttribute('aria-expanded', 'false');
    if (!query) {
      close();
      return;
    }
    panel.hidden = false;
    status.textContent = 'טוען חיפוש…';
    try {
      const pages = await loadIndex();
      if (current !== revision) return;
      const words = query.split(/\s+/);
      results = pages.filter((page) => words.every((word) => page.text.includes(word)))
        .map((page) => ({ ...page, score: page.name === query ? 0
          : page.name.startsWith(query) ? 1 : page.name.includes(query) ? 2 : 3 }))
        .sort((a, b) => a.score - b.score || a.title.localeCompare(b.title, 'he'))
        .slice(0, 10);
      results.forEach((page, i) => {
        const item = document.createElement('li');
        item.id = `search-result-${i}`;
        item.setAttribute('role', 'option');
        item.setAttribute('aria-selected', 'false');
        const link = document.createElement('a');
        link.href = page.url;
        link.tabIndex = -1;
        const title = document.createElement('span');
        title.textContent = page.title;
        const path = document.createElement('small');
        path.textContent = decodeURI(page.url);
        path.dir = 'ltr';
        link.append(title, path);
        item.append(link);
        list.append(item);
      });
      input.setAttribute('aria-expanded', String(results.length > 0));
      status.textContent = results.length ? `מוצגות ${results.length} הצעות` : 'לא נמצאו תוצאות';
    } catch {
      if (current !== revision) return;
      status.textContent = 'לא ניתן לטעון את החיפוש. נסו שוב.';
    }
  }

  input.addEventListener('input', search);
  input.addEventListener('focus', () => {
    if (input.value.trim()) search();
    else loadIndex().catch(() => {});
  });
  input.addEventListener('keydown', (event) => {
    if (event.isComposing) return;
    if (event.key === 'Escape') {
      event.preventDefault();
      close();
    } else if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
      event.preventDefault();
      if (panel.hidden) { search(); return; }
      if (!results.length) return;
      active = active < 0 ? (event.key === 'ArrowDown' ? 0 : results.length - 1)
        : (active + (event.key === 'ArrowDown' ? 1 : -1) + results.length) % results.length;
      Array.from(list.children).forEach((item, i) => {
        item.setAttribute('aria-selected', String(i === active));
      });
      const selected = list.children[active];
      input.setAttribute('aria-activedescendant', selected.id);
      selected.scrollIntoView({ block: 'nearest' });
    } else if (event.key === 'Enter' && !panel.hidden && results.length) {
      event.preventDefault();
      window.location.assign(results[active < 0 ? 0 : active].url);
    } else if (event.key === 'Tab') close();
  });
  root.addEventListener('focusout', (event) => {
    if (!root.contains(event.relatedTarget)) close();
  });
  document.addEventListener('pointerdown', (event) => {
    if (!root.contains(event.target)) close();
  });
  root.hidden = false;
})();
