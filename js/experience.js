/* ==========================================================================
   EDITH experience.js — homepage-only interactive widgets:
   1. The radial "EDITH ecosystem" network diagram
   2. The featured-projects carousel
   3. The nine-stage project-journey stepper
   ========================================================================== */
(function () {
  "use strict";

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  /* ------------------------------------------------------------------
     1. Radial network diagram
     ------------------------------------------------------------------ */
  function initNetwork() {
    var root = $("#edithNetwork");
    var svg = $("#networkLines");
    var detail = $("#networkDetail");
    if (!root || !svg || !detail) return;

    var hub = $(".network__hub", root);
    var nodes = $$(".network__node", root);
    var panels = $$(".network__detail-panel", detail);
    var activeStream = detail.getAttribute("data-active") || (nodes[0] && nodes[0].dataset.stream) || "01";

    function drawLines() {
      var netRect = root.getBoundingClientRect();
      if (!netRect.width || !netRect.height) return;
      var hubRect = hub.getBoundingClientRect();
      var scaleX = 800 / netRect.width;
      var scaleY = 800 / netRect.height;
      var hubX = (hubRect.left + hubRect.width / 2 - netRect.left) * scaleX;
      var hubY = (hubRect.top + hubRect.height / 2 - netRect.top) * scaleY;

      svg.innerHTML = "";
      nodes.forEach(function (node) {
        var r = node.getBoundingClientRect();
        var nx = (r.left + r.width / 2 - netRect.left) * scaleX;
        var ny = (r.top + r.height / 2 - netRect.top) * scaleY;
        var path = document.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", "M " + hubX + " " + hubY + " L " + nx + " " + ny);
        if (node.dataset.stream === activeStream) path.setAttribute("data-active", "true");
        svg.appendChild(path);
      });
    }

    function setActive(stream, opts) {
      opts = opts || {};
      activeStream = stream;

      nodes.forEach(function (node) {
        node.setAttribute("aria-pressed", String(node.dataset.stream === stream));
      });

      panels.forEach(function (panel) {
        var isMatch = panel.dataset.stream === stream;
        if (isMatch) panel.removeAttribute("hidden");
        else panel.setAttribute("hidden", "");
      });

      detail.setAttribute("data-active", stream);

      if (!opts.skipRedraw) {
        /* Nodes animate to their pressed position; redraw the connecting
           lines once that transition has settled. */
        setTimeout(drawLines, 420);
      }
    }

    nodes.forEach(function (node) {
      node.addEventListener("click", function () {
        if (node.dataset.stream === activeStream) return;
        setActive(node.dataset.stream);
      });
    });

    /* Initial state: make sure the node matching the panel already
       visible in the markup is marked pressed, and draw the lines once
       layout has settled (fonts/webfont swap can shift positions). */
    setActive(activeStream, { skipRedraw: true });
    drawLines();

    var resizeTimer;
    window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(drawLines, 150);
    });

    /* Layout can still be settling shortly after load (webfonts etc.) */
    window.addEventListener("load", drawLines);
    setTimeout(drawLines, 600);
  }

  /* ------------------------------------------------------------------
     2. Featured projects carousel
     ------------------------------------------------------------------ */
  function initCarousel() {
    var track = $("#carouselTrack");
    var prev = $("#carouselPrev");
    var next = $("#carouselNext");
    if (!track) return;

    function cardStep() {
      var card = $(".pcard", track);
      if (!card) return track.clientWidth;
      var style = window.getComputedStyle(track);
      var gap = parseFloat(style.columnGap || style.gap || "0") || 0;
      return card.getBoundingClientRect().width + gap;
    }

    if (prev) prev.addEventListener("click", function () {
      track.scrollBy({ left: -cardStep(), behavior: "smooth" });
    });
    if (next) next.addEventListener("click", function () {
      track.scrollBy({ left: cardStep(), behavior: "smooth" });
    });

    /* Animate each card's progress bar to width once it's actually
       visible, instead of firing everything on page load. */
    var bars = $$(".pcard__progress-bar", track);
    if (bars.length && "IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });
      bars.forEach(function (bar) { io.observe(bar); });
    } else {
      bars.forEach(function (bar) { bar.classList.add("is-visible"); });
    }
  }

  /* ------------------------------------------------------------------
     3. Project-journey stepper
     ------------------------------------------------------------------ */
  function initJourney() {
    var widget = $("#journeyWidget");
    var progress = $("#journeyProgress");
    if (!widget || !progress) return;

    var stages = $$(".journey__stage", widget);
    var panels = $$(".journey__panel", widget);
    var track = $(".journey__track", widget);

    function moveProgressTo(stageBtn) {
      var trackRect = track.getBoundingClientRect();
      var btnRect = stageBtn.getBoundingClientRect();
      progress.style.left = (btnRect.left - trackRect.left + track.scrollLeft) + "px";
      progress.style.width = btnRect.width + "px";
    }

    function setStage(num) {
      stages.forEach(function (btn) {
        var isMatch = btn.dataset.stage === num;
        btn.setAttribute("aria-selected", String(isMatch));
        if (isMatch) moveProgressTo(btn);
      });
      panels.forEach(function (panel) {
        if (panel.dataset.stage === num) panel.removeAttribute("hidden");
        else panel.setAttribute("hidden", "");
      });
    }

    stages.forEach(function (btn) {
      btn.addEventListener("click", function () {
        setStage(btn.dataset.stage);
        btn.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
      });
    });

    var initial = stages.find(function (b) { return b.getAttribute("aria-selected") === "true"; }) || stages[0];
    if (initial) setStage(initial.dataset.stage);

    var resizeTimer;
    window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () {
        var current = stages.find(function (b) { return b.getAttribute("aria-selected") === "true"; });
        if (current) moveProgressTo(current);
      }, 150);
    });
  }

  ready(function () {
    initNetwork();
    initCarousel();
    initJourney();
  });
})();
