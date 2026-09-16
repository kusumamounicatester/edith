/* EDITH — JV Sharing Calculator (brief §6.2). Purely a contribution-weighted
   starting point for a conversation — never presented as a binding split. */
document.addEventListener('DOMContentLoaded', function () {
  var form = document.getElementById('jvCalcForm');
  if (!form) return;
  var resultBox = document.getElementById('jvResult');
  var splitEl = document.getElementById('jvSplit');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var land = parseFloat(document.getElementById('jv-land').value) || 0;
    var cash = parseFloat(document.getElementById('jv-cash').value) || 0;
    var edith = parseFloat(document.getElementById('jv-edith').value) || 0;

    var partnerTotal = land + cash;
    var grandTotal = partnerTotal + edith;
    if (grandTotal <= 0) return;

    var partnerShare = Math.round((partnerTotal / grandTotal) * 100);
    var edithShare = 100 - partnerShare;

    splitEl.textContent = 'Roughly ' + partnerShare + '% : ' + edithShare + '% (you : EDITH)';
    resultBox.hidden = false;
    resultBox.setAttribute('tabindex', '-1');
    resultBox.focus();
  });
});
