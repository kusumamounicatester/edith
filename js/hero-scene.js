/* ==========================================================================
   EDITH hero-scene.js — subtle pointer-parallax for the hero's blueprint
   SVG and coordinate readout. Loaded as a module (see index.html) so it
   can be upgraded to a full three.js scene later without touching the
   markup — the import map for three@0.186.0 is already in <head> and
   ready to use, but this file intentionally has no dependency on it: a
   WebGL scene is a nice-to-have, and shouldn't be a hard requirement for
   the hero to look finished. #heroScene / .hero__scene stays inert
   (opacity 0 per homepage.css) until something sets it up.
   ========================================================================== */
(function () {
  "use strict";

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  ready(function () {
    var hero = document.getElementById("hero");
    var blueprint = document.querySelector(".hero__blueprint");
    var coords = document.getElementById("heroCoords");
    if (!hero) return;

    var reduceMotion = window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var isCoarsePointer = window.matchMedia &&
      window.matchMedia("(pointer: coarse)").matches;
    if (reduceMotion || isCoarsePointer) return; /* respect motion prefs / touch devices */

    var targets = [blueprint, coords].filter(Boolean);
    if (!targets.length) return;

    var raf = null;
    function onMove(e) {
      var rect = hero.getBoundingClientRect();
      var relX = (e.clientX - rect.left) / rect.width - 0.5;  /* -0.5..0.5 */
      var relY = (e.clientY - rect.top) / rect.height - 0.5;

      if (raf) return;
      raf = requestAnimationFrame(function () {
        targets.forEach(function (el) {
          var depth = Number(el.getAttribute("data-depth")) || 12;
          var x = (relX * depth).toFixed(2);
          var y = (relY * depth).toFixed(2);
          el.style.transform = "translate(" + x + "px, " + y + "px)";
        });
        raf = null;
      });
    }

    hero.addEventListener("mousemove", onMove);
    hero.addEventListener("mouseleave", function () {
      targets.forEach(function (el) { el.style.transform = ""; });
    });
  });
})();
