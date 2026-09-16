/* ==========================================================================
   EDITH calculator.js — homepage "cost intelligence" teaser widget.
   Indicative-only construction cost estimate: builtUpArea × rate(tier) ×
   floors, split into a material/labour breakdown. Placeholder rates —
   marked as such in the UI and in the disclaimer already present in the
   markup; swap RATES for EDITH's confirmed, region-accurate figures
   before go-live.
   ========================================================================== */
(function () {
  "use strict";

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  var RATES = { basic: 1450, standard: 1850, premium: 2400 };
  var MATERIAL_SHARE = 0.62; /* indicative material : labour split */

  function formatINR(n) {
    var rounded = Math.round(n);
    /* Indian digit grouping: last 3 digits, then groups of 2 */
    var s = String(rounded);
    var isNeg = s[0] === "-";
    if (isNeg) s = s.slice(1);
    var last3 = s.slice(-3);
    var rest = s.slice(0, -3);
    if (rest !== "") last3 = "," + last3;
    var grouped = rest.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + last3;
    return (isNeg ? "-₹" : "₹") + grouped;
  }

  function initCalculator() {
    var form = $("#costCalcForm");
    if (!form) return;

    var areaInput = $("#builtUpArea", form);
    var areaOut = $("#builtUpAreaOut");
    var floorsInput = $("#floors", form);
    var floorsOut = $("#floorsOut");
    var tierSelect = $("#qualityTier", form);

    var result = $("#calcResult");
    var totalEl = $("#calcTotal");
    var rateEl = $("#calcRate");
    var materialBar = $("#calcMaterialBar");
    var laborBar = $("#calcLaborBar");
    var materialVal = $("#calcMaterialVal");
    var laborVal = $("#calcLaborVal");

    function syncOutputs() {
      if (areaOut && areaInput) areaOut.textContent = Number(areaInput.value).toLocaleString("en-IN");
      if (floorsOut && floorsInput) floorsOut.textContent = floorsInput.value;
    }
    syncOutputs();
    if (areaInput) areaInput.addEventListener("input", syncOutputs);
    if (floorsInput) floorsInput.addEventListener("input", syncOutputs);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!areaInput || !floorsInput || !tierSelect) return;

      var area = Number(areaInput.value) || 0;
      var floors = Number(floorsInput.value) || 1;
      var tier = tierSelect.value;
      var rate = RATES[tier] || RATES.standard;

      var total = area * rate * floors;
      var material = total * MATERIAL_SHARE;
      var labor = total - material;

      if (totalEl) totalEl.textContent = formatINR(total);
      if (rateEl) {
        rateEl.textContent = formatINR(rate) + "/sq.ft × " + area.toLocaleString("en-IN") +
          " sq.ft × " + floors + (floors > 1 ? " floors" : " floor");
      }
      if (materialBar) materialBar.style.width = Math.round(MATERIAL_SHARE * 100) + "%";
      if (laborBar) laborBar.style.width = Math.round((1 - MATERIAL_SHARE) * 100) + "%";
      if (materialVal) materialVal.textContent = formatINR(material);
      if (laborVal) laborVal.textContent = formatINR(labor);

      if (result) {
        result.hidden = false;
        result.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    });
  }

  ready(initCalculator);
})();
