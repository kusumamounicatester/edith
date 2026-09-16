/* EDITH — Consumer Services Quote Wizard (brief §6.4).
   Steps: service type -> parameters -> location -> contact -> instant estimate. */
document.addEventListener('DOMContentLoaded', function () {
  var wizard = document.getElementById('quoteWizard');
  if (!wizard) return;

  var panels = wizard.querySelectorAll('.wizard__panel');
  var steps = wizard.querySelectorAll('.wizard__steps span');
  var serviceSelect = document.getElementById('q-service');
  var paramBlocks = {
    construction: document.getElementById('paramsConstruction'),
    interiors: document.getElementById('paramsInteriors'),
    borewell: document.getElementById('paramsBorewell')
  };

  function goToStep(n) {
    panels.forEach(function (p) { p.classList.toggle('is-active', p.dataset.panel === String(n)); });
    steps.forEach(function (s) { s.classList.toggle('is-active', s.dataset.step === String(n)); });
  }

  wizard.querySelectorAll('[data-next]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var current = wizard.querySelector('.wizard__panel.is-active');
      var next = parseInt(current.dataset.panel, 10) + 1;
      goToStep(next);
    });
  });
  wizard.querySelectorAll('[data-prev]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var current = wizard.querySelector('.wizard__panel.is-active');
      var prev = parseInt(current.dataset.panel, 10) - 1;
      goToStep(prev);
    });
  });

  if (serviceSelect) {
    serviceSelect.addEventListener('change', function () {
      Object.keys(paramBlocks).forEach(function (key) {
        paramBlocks[key].hidden = key !== serviceSelect.value;
      });
    });
  }

  // Instant indicative estimate — a light-weight version of the same idea as
  // calculator.js's RATE_TABLE. Same PLACEHOLDER-rates caveat applies (§8).
  var RATES = {
    construction: 1850, // per sq.ft, standard tier — placeholder
    interiors: 45000,   // per room — placeholder
    borewell: 90        // per ft depth — placeholder
  };

  var form = wizard.querySelector('form[data-module="consumer-quote"]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var service = serviceSelect.value;
      var estimate = 0;
      if (service === 'construction') {
        estimate = (parseFloat(document.getElementById('q-area').value) || 0) * RATES.construction;
      } else if (service === 'interiors') {
        estimate = (parseFloat(document.getElementById('q-rooms').value) || 0) * RATES.interiors;
      } else if (service === 'borewell') {
        estimate = (parseFloat(document.getElementById('q-depth').value) || 0) * RATES.borewell;
      }
      var estimateEl = document.getElementById('quoteEstimateValue');
      var estimateBox = document.getElementById('quoteEstimate');
      if (estimateEl && estimateBox) {
        estimateEl.textContent = '≈ ₹' + Math.round(estimate).toLocaleString('en-IN');
        estimateBox.hidden = false;
      }
      // TODO: POST to the CRM lead-capture endpoint once §10 backend exists.
    });
  }
});
