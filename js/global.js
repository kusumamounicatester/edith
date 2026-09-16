/* ==========================================================================
   EDITH global.js — sitewide behaviour (every page, not just the homepage)
   Owns: mobile nav + dropdowns, sticky header condensing, scroll-reveal
   ([data-reveal], see global.css), header search overlay, the EN/Telugu
   language toggle, and the live clock in the hero coordinates strip.
   Depends on window.EDITH_I18N_TE from js/i18n-te.js when present.
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
     0. Small helpers
     ------------------------------------------------------------------ */
  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  /* ------------------------------------------------------------------
     1. Mobile nav toggle
     ------------------------------------------------------------------ */
  function initMobileNav() {
    var toggle = $("#navToggle");
    var nav = $("#mainNav");
    if (!toggle || !nav) return;

    function closeNav() {
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
    }
    function openNav() {
      nav.classList.add("is-open");
      toggle.setAttribute("aria-expanded", "true");
    }

    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.contains("is-open");
      if (isOpen) closeNav(); else openNav();
    });

    /* Close the mobile drawer automatically once the viewport grows past
       the breakpoint where the drawer CSS stops applying, so the menu
       doesn't stay "open" (and unusable) if the user resizes/rotates. */
    var mq = window.matchMedia("(max-width: 900px)");
    function handleBreakpoint(e) { if (!e.matches) closeNav(); }
    if (mq.addEventListener) mq.addEventListener("change", handleBreakpoint);
    else if (mq.addListener) mq.addListener(handleBreakpoint);

    /* Close on Escape */
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        closeNav();
        toggle.focus();
      }
    });
  }

  /* ------------------------------------------------------------------
     2. Nav dropdowns ("Collaborate ▾", "Services ▾", …)
     Works on hover+focus on desktop (CSS already handles that visually
     via :hover/.is-open) and on click/tap + keyboard everywhere, which
     is required for touch devices and for accessibility.
     ------------------------------------------------------------------ */
  function initDropdowns() {
    var items = $$("#mainNav > ul > li").filter(function (li) {
      return li.querySelector(":scope > button[aria-haspopup]");
    });
    if (!items.length) return;

    function closeAll(except) {
      items.forEach(function (li) {
        if (li === except) return;
        li.classList.remove("is-open");
        var btn = li.querySelector(":scope > button[aria-haspopup]");
        if (btn) btn.setAttribute("aria-expanded", "false");
      });
    }

    items.forEach(function (li) {
      var btn = li.querySelector(":scope > button[aria-haspopup]");
      if (!btn) return;

      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var willOpen = !li.classList.contains("is-open");
        closeAll(li);
        li.classList.toggle("is-open", willOpen);
        btn.setAttribute("aria-expanded", String(willOpen));
      });

      li.addEventListener("keydown", function (e) {
        if (e.key === "Escape") {
          li.classList.remove("is-open");
          btn.setAttribute("aria-expanded", "false");
          btn.focus();
        }
      });
    });

    /* Click outside closes everything */
    document.addEventListener("click", function (e) {
      if (!e.target.closest("#mainNav > ul > li")) closeAll();
    });
  }

  /* ------------------------------------------------------------------
     3. Sticky header: condense once the page has scrolled a little
     ------------------------------------------------------------------ */
  function initCondensedHeader() {
    var header = $(".site-header");
    if (!header) return;
    var threshold = 24;
    var ticking = false;

    function update() {
      header.classList.toggle("is-condensed", window.scrollY > threshold);
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }, { passive: true });
    update();
  }

  /* ------------------------------------------------------------------
     4. Header search overlay
     ------------------------------------------------------------------ */
  function initSearchOverlay() {
    var openBtn = $("#searchOpen");
    var closeBtn = $("#searchClose");
    var overlay = $("#searchOverlay");
    if (!openBtn || !overlay) return;
    var input = $("input", overlay);

    function open() {
      overlay.classList.add("is-open");
      if (input) setTimeout(function () { input.focus(); }, 50);
      document.addEventListener("keydown", onKeydown);
    }
    function close() {
      overlay.classList.remove("is-open");
      document.removeEventListener("keydown", onKeydown);
      openBtn.focus();
    }
    function onKeydown(e) { if (e.key === "Escape") close(); }

    openBtn.addEventListener("click", open);
    if (closeBtn) closeBtn.addEventListener("click", close);
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) close();
    });
  }

  /* ------------------------------------------------------------------
     5. Scroll reveal — the fade/rise entrance defined in global.css for
     every [data-reveal] element. Without this observer those elements
     stay at opacity:0 permanently (html.js sets that up), which is why
     whole sections can look "missing" until this runs.
     ------------------------------------------------------------------ */
  function initScrollReveal() {
    var items = $$("[data-reveal]");
    if (!items.length) return;

    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-revealed"); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-revealed");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });

    items.forEach(function (el) { io.observe(el); });
  }

  /* ------------------------------------------------------------------
     6. Hero clock (IST) — purely decorative, degrades silently
     ------------------------------------------------------------------ */
  function initHeroClock() {
    var clock = $("#heroClock");
    if (!clock) return;
    function tick() {
      var now = new Date();
      var ist = new Date(now.toLocaleString("en-US", { timeZone: "Asia/Kolkata" }));
      var hh = String(ist.getHours()).padStart(2, "0");
      var mm = String(ist.getMinutes()).padStart(2, "0");
      var ss = String(ist.getSeconds()).padStart(2, "0");
      clock.textContent = hh + ":" + mm + ":" + ss + " IST";
    }
    tick();
    setInterval(tick, 1000);
  }

  /* ------------------------------------------------------------------
     7. Hero scroll button — smooth-scrolls to the next section
     ------------------------------------------------------------------ */
  function initHeroScrollButton() {
    var btn = $("#heroScrollBtn");
    var hero = $("#hero");
    if (!btn || !hero) return;
    btn.addEventListener("click", function () {
      var next = hero.nextElementSibling;
      if (next) next.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  /* ------------------------------------------------------------------
     8. Language toggle (EN / Telugu)
     - Persists the choice in localStorage so it holds across pages.
     - Caches each translated element's original English markup the
       first time it runs, so switching back to English is exact.
     - Understands two attribute forms:
         data-i18n="t0001"                 → replaces innerHTML
         data-i18n-attr="alt:t0002"         → replaces the given attribute
                                              (repeatable, space-separated
                                              for more than one attribute)
     ------------------------------------------------------------------ */
  var LANG_KEY = "edith_lang";
  var originalsCache = new WeakMap();

  function getDict() {
    return window.EDITH_I18N_TE || {};
  }

  function cacheOriginal(el) {
    if (!originalsCache.has(el)) {
      originalsCache.set(el, { html: el.innerHTML });
    }
  }

  function applyLanguage(lang) {
    var dict = getDict();
    var textEls = $$("[data-i18n]");
    var attrEls = $$("[data-i18n-attr]");

    textEls.forEach(function (el) {
      cacheOriginal(el);
      if (lang === "te") {
        var key = el.getAttribute("data-i18n");
        var val = dict[key];
        if (val) el.innerHTML = val;
      } else {
        el.innerHTML = originalsCache.get(el).html;
      }
    });

    attrEls.forEach(function (el) {
      var pairs = el.getAttribute("data-i18n-attr").split(" ").filter(Boolean);
      pairs.forEach(function (pair) {
        var split = pair.split(":");
        var attr = split[0];
        var key = split[1];
        var cacheKey = "data-i18n-orig-" + attr;
        if (!el.dataset[cacheKey]) {
          el.dataset[cacheKey] = el.getAttribute(attr) || "";
        }
        if (lang === "te" && dict[key]) {
          el.setAttribute(attr, dict[key]);
        } else {
          el.setAttribute(attr, el.dataset[cacheKey]);
        }
      });
    });

    document.documentElement.setAttribute("lang", lang === "te" ? "te" : "en");
    var toggle = $("#langToggle");
    if (toggle) toggle.setAttribute("aria-pressed", String(lang === "te"));
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* private mode etc. */ }
  }

  function initLanguageToggle() {
    var toggle = $("#langToggle");
    if (!toggle) return;

    var stored = "en";
    try { stored = localStorage.getItem(LANG_KEY) || "en"; } catch (e) { /* ignore */ }

    if (stored === "te") applyLanguage("te");

    toggle.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("lang") === "te" ? "te" : "en";
      applyLanguage(current === "te" ? "en" : "te");
    });
  }

  /* ------------------------------------------------------------------
     Boot
     ------------------------------------------------------------------ */
  ready(function () {
    initMobileNav();
    initDropdowns();
    initCondensedHeader();
    initSearchOverlay();
    initScrollReveal();
    initHeroClock();
    initHeroScrollButton();
    initLanguageToggle();
  });
})();
