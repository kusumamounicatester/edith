/* ==========================================================================
   EDITH lead-forms.js — shared handling for the lead-capture forms on the
   collaborate / service / careers pages (class="lead-form"). Not used by
   index.html itself (its only form is the cost calculator, handled in
   calculator.js), but loaded sitewide so it's safe to include everywhere
   and simply does nothing on pages without a .lead-form.

   What it does, per form:
   - Basic required-field + email/phone sanity checks with inline errors
   - A honeypot field (name="company_website", kept visually hidden via
     .visually-hidden in the markup) to cut down on simple bot spam
   - Prevents the default navigation/reload and shows an inline success
     message, so this works before a real backend endpoint is wired in
   ========================================================================== */
(function () {
  "use strict";

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var PHONE_RE = /^[+]?[\d\s().-]{7,15}$/;

  function fieldError(field, message) {
    clearFieldError(field);
    if (!message) return;
    field.setAttribute("aria-invalid", "true");
    var note = document.createElement("p");
    note.className = "lead-form__error";
    note.style.color = "var(--edith-danger, #a5402f)";
    note.style.fontSize = "0.8rem";
    note.style.margin = "0.35rem 0 0";
    note.textContent = message;
    field.insertAdjacentElement("afterend", note);
  }

  function clearFieldError(field) {
    field.removeAttribute("aria-invalid");
    var next = field.nextElementSibling;
    if (next && next.classList.contains("lead-form__error")) next.remove();
  }

  function validateForm(form) {
    var valid = true;
    $$("[required]", form).forEach(function (field) {
      var value = (field.value || "").trim();
      if (!value) {
        fieldError(field, "This field is required.");
        valid = false;
      } else if (field.type === "email" && !EMAIL_RE.test(value)) {
        fieldError(field, "Enter a valid email address.");
        valid = false;
      } else if (field.type === "tel" && !PHONE_RE.test(value)) {
        fieldError(field, "Enter a valid phone number.");
        valid = false;
      } else {
        clearFieldError(field);
      }
    });
    return valid;
  }

  function showSuccess(form) {
    var wrap = document.createElement("div");
    wrap.className = "lead-form__success";
    wrap.setAttribute("role", "status");
    wrap.style.padding = "1rem 1.25rem";
    wrap.style.marginTop = "1rem";
    wrap.style.border = "1px solid var(--edith-gold-600, #B9873D)";
    wrap.style.background = "var(--edith-paper-100, #F1EEE5)";
    wrap.style.fontSize = "0.9rem";
    wrap.textContent = "Thanks — we've got your details and someone from EDITH will be in touch shortly.";
    form.hidden = true;
    form.insertAdjacentElement("afterend", wrap);
    wrap.focus && wrap.focus();
  }

  function initForm(form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      /* Honeypot: if a bot filled this hidden field in, silently no-op
         but still look successful so it doesn't learn anything. */
      var honeypot = $('[name="company_website"]', form);
      if (honeypot && honeypot.value) {
        showSuccess(form);
        return;
      }

      if (!validateForm(form)) {
        var firstInvalid = $("[aria-invalid='true']", form);
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      /* No backend wired up yet — this is where a fetch() POST to the
         real lead-capture endpoint belongs once it exists. */
      showSuccess(form);
    });

    /* Clear an individual field's error as soon as it's corrected */
    $$("[required]", form).forEach(function (field) {
      field.addEventListener("input", function () { clearFieldError(field); });
    });
  }

  ready(function () {
    $$(".lead-form").forEach(initForm);
  });
})();
