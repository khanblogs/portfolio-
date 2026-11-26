// Portfolio v2 — progressive enhancement only; the site is complete without it.
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }
  // Marquee duplication (decorative)
  var t = document.getElementById('marqueeTrack');
  if (t) { t.innerHTML += t.innerHTML; t.querySelectorAll('img').forEach(function (i) { i.setAttribute('aria-hidden', 'true'); i.alt = ''; }); }
  // Time-zone clocks (numbers are aria-hidden; band is decorative context)
  var cells = document.querySelectorAll('.tz-cell .t[data-tz]');
  if (cells.length) {
    var tick = function () {
      cells.forEach(function (c) {
        try { c.textContent = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false, timeZone: c.getAttribute('data-tz') }).format(new Date()); } catch (e) {}
      });
    };
    tick(); setInterval(tick, 1000);
  }
  // Reading progress + back-to-top
  var bar = document.getElementById('progressBar'), top = document.getElementById('toTop');
  var onScroll = function () {
    var h = document.documentElement, max = h.scrollHeight - h.clientHeight;
    if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? (h.scrollTop / max) : 0) + ')';
    if (top) top.classList.toggle('show', h.scrollTop > 600);
  };
  document.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  if (top) top.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });
  // Topology captions
  var cap = document.getElementById('topoCap');
  if (cap) {
    document.querySelectorAll('.tnode').forEach(function (n) {
      var show = function () { cap.textContent = n.getAttribute('data-cap'); };
      n.addEventListener('mouseenter', show); n.addEventListener('focus', show);
    });
  }
  // Hero cursor glow (fine pointers only)
  var glow = document.getElementById('cursorGlow'), hero = document.querySelector('.hero');
  if (glow && hero && window.matchMedia('(pointer: fine)').matches && !reduce) {
    hero.addEventListener('mousemove', function (e) {
      var r = hero.getBoundingClientRect();
      glow.style.background = 'radial-gradient(420px circle at ' + (e.clientX - r.left) + 'px ' + (e.clientY - r.top) + 'px, rgba(212,175,55,0.08), transparent 65%)';
    });
  }
})();
