/* Laybond — site interactions (no libraries needed) */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  /* ---- Years since founding (e.g. data-since="1994") – updates automatically every year ---- */
  Array.prototype.forEach.call(document.querySelectorAll("[data-since]"), function (el) {
    var n = new Date().getFullYear() - parseInt(el.getAttribute("data-since"), 10);
    el.textContent = n;
    if (el.hasAttribute("data-count")) el.setAttribute("data-count", n);
  });

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- Remove broken images so the placeholder shows through ---- */
  $$(".media img").forEach(function (img) {
    function fail() { img.remove(); }
    if (img.complete && img.naturalWidth === 0) fail();
    else img.addEventListener("error", fail);
  });
  $$(".media video").forEach(function (v) {
    var src = v.querySelector("source");
    if (src) src.addEventListener("error", function () { v.remove(); });
    v.addEventListener("error", function () { v.remove(); });
    if (reduceMotion) { v.removeAttribute("autoplay"); v.pause && v.pause(); }
  });

  /* ---- Header: solid background after scrolling ---- */
  var header = $(".site-header");
  var toTop = $(".float-btn--top");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 30);
    if (toTop) toTop.classList.toggle("is-visible", y > 700);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function (e) { e.preventDefault(); window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }); });

  /* ---- Mobile menu ---- */
  var toggle = $(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open);
    });
  }

  /* ---- Products dropdown ---- */
  $$(".nav-drop").forEach(function (drop) {
    var btn = $("button", drop);
    var hoverable = window.matchMedia("(hover: hover) and (min-width: 961px)");
    var timer;
    function set(open) { drop.classList.toggle("is-open", open); btn.setAttribute("aria-expanded", open); }
    btn.addEventListener("click", function (e) { e.stopPropagation(); set(!drop.classList.contains("is-open")); });
    drop.addEventListener("mouseenter", function () { if (hoverable.matches) { clearTimeout(timer); set(true); } });
    drop.addEventListener("mouseleave", function () { if (hoverable.matches) timer = setTimeout(function () { set(false); }, 180); });
    document.addEventListener("click", function (e) { if (!drop.contains(e.target) && hoverable.matches) set(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { set(false); } });
  });

  /* ---- Reveal on scroll ---- */
  var reveals = $$(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---- Count-up numbers ---- */
  var counters = $$("[data-count]");
  function runCounter(el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var dur = 1600, start = null;
    function step(t) {
      if (!start) start = t;
      var p = Math.min((t - start) / dur, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))).toLocaleString("en-IN");
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window && !reduceMotion) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { runCounter(en.target); cio.unobserve(en.target); } });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---- Accordion ---- */
  $$(".acc-item").forEach(function (item) {
    var btn = $(".acc-btn", item);
    btn.addEventListener("click", function () {
      var open = !item.classList.contains("is-open");
      item.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open);
    });
  });

  /* ---- Gallery (data from assets/js/gallery-data.js) ---- */
  var grid = $("#gallery-grid");
  var items = window.LAYBOND_GALLERY || [];
  var icons = {
    play: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
  };
  function esc(s) { return String(s || "").replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  if (grid) {
    var limit = parseInt(grid.getAttribute("data-limit") || "0", 10);
    var list = limit ? items.filter(function (i) { return i.featured; }).slice(0, limit) : items;
    if (limit && list.length < limit) list = items.slice(0, limit);
    grid.innerHTML = list.map(function (it, idx) {
      var isVideo = it.type === "video";
      var thumb = it.thumb || (isVideo ? it.poster : it.src);
      return '<button type="button" class="g-item' + (it.wide ? " is-wide" : "") + '" data-cat="' + esc(it.category) + '" data-index="' + idx + '">' +
        '<div class="media" data-label="' + esc(it.title) + '">' +
        (thumb ? '<img src="' + esc(thumb) + '" alt="' + esc(it.title) + '" loading="lazy">' : "") + "</div>" +
        (isVideo ? '<span class="g-play">' + icons.play + "</span>" : "") +
        '<span class="g-cap"><small>' + esc(it.categoryLabel || it.category) + "</small>" + esc(it.title) + "</span></button>";
    }).join("");
    $$(".media img", grid).forEach(function (img) {
      img.addEventListener("error", function () { img.remove(); });
    });

    // Filters
    $$(".filter").forEach(function (f) {
      f.addEventListener("click", function () {
        $$(".filter").forEach(function (x) { x.classList.remove("is-active"); x.setAttribute("aria-pressed", "false"); });
        f.classList.add("is-active"); f.setAttribute("aria-pressed", "true");
        var cat = f.getAttribute("data-filter");
        $$(".g-item", grid).forEach(function (g) {
          var match = cat === "all" || g.getAttribute("data-cat") === cat || (cat === "video" && list[+g.getAttribute("data-index")].type === "video");
          g.hidden = !match;
        });
      });
    });

    // Lightbox
    var lb = $("#lightbox"), lbStage = $("#lb-stage"), lbCap = $("#lb-cap"), current = 0;
    function visible() { return $$(".g-item", grid).filter(function (g) { return !g.hidden; }); }
    function show(idx) {
      current = idx;
      var it = list[idx];
      var html;
      if (it.type === "video") {
        html = '<video src="' + esc(it.src) + '" controls autoplay playsinline' + (it.poster ? ' poster="' + esc(it.poster) + '"' : "") + "></video>";
      } else {
        html = '<img src="' + esc(it.src) + '" alt="' + esc(it.title) + '">';
      }
      lbStage.innerHTML = html;
      var m = lbStage.firstChild;
      m.addEventListener("error", function () { lbStage.innerHTML = '<div class="media lb-empty" data-label="Add file: ' + esc(it.src) + '"></div>'; });
      lbCap.textContent = it.title + (it.caption ? " — " + it.caption : "");
    }
    function open(idx) { show(idx); lb.classList.add("is-open"); document.body.style.overflow = "hidden"; $(".lb-close", lb).focus(); }
    function close() { lb.classList.remove("is-open"); lbStage.innerHTML = ""; document.body.style.overflow = ""; }
    function step(d) {
      var v = visible().map(function (g) { return +g.getAttribute("data-index"); });
      var pos = v.indexOf(current);
      show(v[(pos + d + v.length) % v.length]);
    }
    if (lb) {
      grid.addEventListener("click", function (e) {
        var g = e.target.closest(".g-item");
        if (g) open(+g.getAttribute("data-index"));
      });
      $(".lb-close", lb).addEventListener("click", close);
      $(".lb-prev", lb).addEventListener("click", function () { step(-1); });
      $(".lb-next", lb).addEventListener("click", function () { step(1); });
      lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
      document.addEventListener("keydown", function (e) {
        if (!lb.classList.contains("is-open")) return;
        if (e.key === "Escape") close();
        if (e.key === "ArrowRight") step(1);
        if (e.key === "ArrowLeft") step(-1);
      });
    }
  }

  /* ---- Contact form ---- */
  var form = $("#contact-form");
  if (form) {
    var started = $("input[name=ts]", form);
    if (started) started.value = Date.now();
    var status = $(".form-status", form);
    var params = new URLSearchParams(location.search);
    var product = params.get("product");
    if (product && form.product) form.product.value = product;

    function validate() {
      var ok = true;
      $$("[required]", form).forEach(function (el) {
        var f = el.closest(".field");
        var bad = !el.value.trim() || (el.type === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value)) ||
          (el.name === "phone" && el.value.replace(/\D/g, "").length < 10);
        if (f) f.classList.toggle("has-error", bad);
        if (bad && ok) { el.focus(); ok = false; }
      });
      return ok;
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "form-status";
      if (!validate()) return;
      var btn = $("button[type=submit]", form), label = btn.innerHTML;
      btn.disabled = true; btn.textContent = "Sending…";
      fetch(form.action, { method: "POST", body: new FormData(form), headers: { "X-Requested-With": "fetch" } })
        .then(function (r) { return r.json().catch(function () { return { ok: r.ok }; }); })
        .then(function (res) {
          if (res.ok) {
            form.reset();
            status.className = "form-status is-success";
            status.textContent = "Thank you! Your enquiry has been sent. Our team will get back to you within one working day.";
          } else {
            status.className = "form-status is-error";
            status.textContent = res.error || "Sorry, something went wrong. Please call us or email sales@laybond.co.in.";
          }
        })
        .catch(function () {
          status.className = "form-status is-error";
          status.textContent = "Could not send right now. Please call +91 98400 32218 or email sales@laybond.co.in.";
        })
        .finally(function () { btn.disabled = false; btn.innerHTML = label; if (started) started.value = Date.now() - 10000; });
    });
  }

  /* ---- Current year ---- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
