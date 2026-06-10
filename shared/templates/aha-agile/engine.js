/* ============================================================
   AHA AGILE — DECK ENGINE SCRIPT  ·  DO NOT MODIFY PER DECK
   Keyboard nav, hash deep-links (#3 or #/3, 1-based), grid
   overview (G), fullscreen (F), auto-fading controls.
   Controls stay hidden until the mouse moves, so headless
   screenshots capture clean slides.
   ============================================================ */
(function () {
  const slides = [...document.querySelectorAll('.slide')];
  const stage = document.querySelector('.stage');
  const nowEl = document.getElementById('now');
  const totalEl = document.getElementById('total');
  const tnameEl = document.getElementById('tname');
  let i = 0;
  let chromeTimer = null;

  if (totalEl) totalEl.textContent = String(slides.length).padStart(2, '0');

  function pad(n) { return String(n + 1).padStart(2, '0'); }

  function show(n, skipHash) {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => s.classList.toggle('active', k === i));
    if (nowEl) nowEl.textContent = pad(i);
    if (tnameEl) tnameEl.textContent = slides[i].dataset.type ? '· ' + slides[i].dataset.type : '';
    if (!skipHash) history.replaceState(null, '', '#' + (i + 1));
  }

  function fromHash() {
    const m = location.hash.match(/(\d+)/);
    return m ? Math.min(Math.max(parseInt(m[1], 10) - 1, 0), slides.length - 1) : 0;
  }

  function fit() {
    if (document.body.classList.contains('grid')) return;
    const s = Math.min(window.innerWidth / 1280, window.innerHeight / 720);
    stage.style.transform = 'scale(' + s + ')';
  }

  function toggleGrid() {
    document.body.classList.toggle('grid');
    if (document.body.classList.contains('grid')) { stage.style.transform = 'none'; }
    else { fit(); show(i); }
  }

  function wakeChrome() {
    document.body.classList.add('chrome');
    clearTimeout(chromeTimer);
    chromeTimer = setTimeout(() => document.body.classList.remove('chrome'), 2500);
  }

  const btnNext = document.getElementById('next');
  const btnPrev = document.getElementById('prev');
  const btnGrid = document.getElementById('grid');
  if (btnNext) btnNext.onclick = () => show(i + 1);
  if (btnPrev) btnPrev.onclick = () => show(i - 1);
  if (btnGrid) btnGrid.onclick = toggleGrid;

  // click a thumbnail in grid mode to open it
  slides.forEach((s, k) => s.addEventListener('click', () => {
    if (document.body.classList.contains('grid')) {
      document.body.classList.remove('grid');
      fit();
      show(k);
    }
  }));

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); show(i + 1); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(i - 1); }
    else if (e.key === 'Home') { show(0); }
    else if (e.key === 'End') { show(slides.length - 1); }
    else if (e.key.toLowerCase() === 'g') { toggleGrid(); }
    else if (e.key.toLowerCase() === 'f') {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else document.exitFullscreen();
    }
  });

  window.addEventListener('resize', fit);
  window.addEventListener('hashchange', () => show(fromHash(), true));
  document.addEventListener('mousemove', wakeChrome);

  fit();
  show(fromHash(), true);
})();
