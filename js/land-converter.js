/* EDITH — Land-unit converter (brief §8). Conversion factors are standard
   and NOT region-variable like pricing — safe to leave as-is, unlike the
   RATE_TABLE values in calculator.js. */
var SQFT_PER_UNIT = {
  sqft: 1,
  sqyd: 9,
  acre: 43560,
  cent: 435.6,
  gunta: 1089 // 1 gunta = 1/40 acre in most AP/Telangana usage
};

document.addEventListener('DOMContentLoaded', function () {
  var form = document.getElementById('landConvForm');
  if (!form) return;
  var resultBox = document.getElementById('landConvResult');
  var out = document.getElementById('landConvOut');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var value = parseFloat(document.getElementById('lc-value').value) || 0;
    var unit = document.getElementById('lc-unit').value;
    var sqft = value * SQFT_PER_UNIT[unit];

    var lines = Object.keys(SQFT_PER_UNIT)
      .filter(function (u) { return u !== unit; })
      .map(function (u) {
        var converted = sqft / SQFT_PER_UNIT[u];
        return converted.toLocaleString('en-IN', { maximumFractionDigits: 2 }) + ' ' + u;
      });

    out.textContent = lines.join(' · ');
    resultBox.hidden = false;
  });
});
