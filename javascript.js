/* =========================================================
   IRONPULSE GYM - js/main.js  (har page par chalta hai)
   Har feature sirf tab chalta hai jab uska element page par ho.
   ========================================================= */
"use strict";
document.addEventListener("DOMContentLoaded", () => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const store = {
    get(k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* ignore */ } },
    del(k) { try { localStorage.removeItem(k); } catch (e) { /* ignore */ } }
  };

  /* 1. Mobile menu */
  const btn = $(".menu-btn"), nav = $("#nav");
  if (btn) btn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open);
  });

  /* 2. Back-to-top button */
  const top = $("#toTop");
  const onScroll = () => top.classList.toggle("show", window.scrollY > 500);
  window.addEventListener("scroll", onScroll, { passive: true });
  top.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

  /* 3. Counters (0 se target tak) */
  const counters = $$("[data-count]");
  if (counters.length) {
    const io = new IntersectionObserver((entries, obs) => entries.forEach(en => {
      if (!en.isIntersecting) return;
      const el = en.target, end = +el.dataset.count, t0 = performance.now();
      const tick = now => {
        const p = Math.min((now - t0) / 1500, 1);
        el.textContent = Math.floor(p * end).toLocaleString() + (el.dataset.suffix || "");
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      obs.unobserve(el);
    }), { threshold: 0.6 });
    counters.forEach(c => io.observe(c));
  }

  /* 4. Filter buttons (programs aur classes page) */
  $$(".chips[data-target]").forEach(group => {
    const items = $$(group.dataset.target);
    group.addEventListener("click", e => {
      const b = e.target.closest("button");
      if (!b) return;
      $$("button", group).forEach(x => x.classList.toggle("on", x === b));
      items.forEach(it => it.classList.toggle("hidden", b.dataset.filter !== "all" && it.dataset.cat !== b.dataset.filter));
    });
  });

  /* 5. FAQ search */
  const faqSearch = $("#faqSearch");
  if (faqSearch) faqSearch.addEventListener("input", () => {
    const q = faqSearch.value.trim().toLowerCase();
    let n = 0;
    $$(".faq-item").forEach(d => { const ok = d.textContent.toLowerCase().includes(q); d.classList.toggle("hidden", !ok); if (ok) n++; });
    $("#faqEmpty").classList.toggle("hidden", n > 0);
  });

  /* 6. Pricing toggle */
  const billing = $("#billing");
  if (billing) billing.addEventListener("change", () => {
    $$("[data-m]").forEach(el => { el.textContent = billing.checked ? Math.round(el.dataset.y / 12) : el.dataset.m; });
    $$(".per").forEach(p => { p.textContent = billing.checked ? "/mo, billed yearly" : "/month"; });
  });

  /* 7. BMI + calorie calculators */
  const out = (el, html) => { el.innerHTML = html; };
  const bmiForm = $("#bmiForm");
  if (bmiForm) bmiForm.addEventListener("submit", e => {
    e.preventDefault();
    const w = +$("#bw").value, h = +$("#bh").value / 100, box = $("#bmiOut");
    if (!(w >= 20 && w <= 300 && h >= 1 && h <= 2.5)) return out(box, "Please enter valid weight and height.");
    const bmi = w / (h * h);
    const cat = bmi < 18.5 ? ["Underweight", "Focus on strength training and a protein-rich diet."]
      : bmi < 25 ? ["Healthy", "Great! Keep a mix of strength and cardio."]
      : bmi < 30 ? ["Overweight", "Try HIIT and cardio 3-4 times a week."]
      : ["Obese", "Start slow with a trainer and low-impact cardio."];
    out(box, "Your BMI is <b>" + bmi.toFixed(1) + "</b> (" + cat[0] + "). " + cat[1]);
  });
  const calForm = $("#calForm");
  if (calForm) calForm.addEventListener("submit", e => {
    e.preventDefault();
    const w = +$("#cw").value, h = +$("#ch").value, a = +$("#ca").value, box = $("#calOut");
    if (!(w > 20 && h > 100 && a >= 12 && a <= 90)) return out(box, "Please enter valid values.");
    const bmr = 10 * w + 6.25 * h - 5 * a + ($("#cg").value === "m" ? 5 : -161);
    const tdee = bmr * +$("#cact").value, goal = +$("#cgoal").value;
    out(box, "Maintenance: <b>" + Math.round(tdee) + " kcal/day</b>. For your goal eat about <b>" + Math.round(tdee + goal) + " kcal/day</b>.");
  });

  /* 8. Gallery lightbox */
  const dlg = $("#lb");
  if (dlg) {
    $$(".tile").forEach(t => t.addEventListener("click", () => {
      $("#lbTitle").textContent = t.textContent.trim();
      $("#lbText").textContent = t.dataset.caption;
      dlg.showModal();
    }));
    $("#lbClose").addEventListener("click", () => dlg.close());
    dlg.addEventListener("click", e => { if (e.target === dlg) dlg.close(); });
  }

  /* 9. Form validation (har <form data-validate>) */
  $$("form[data-validate]").forEach(form => {
    const fields = $$("input[required], select[required], textarea[required]", form);
    const check = el => {
      const ok = el.checkValidity();
      el.closest(".field").classList.toggle("bad", !ok);
      return ok;
    };
    fields.forEach(el => { el.addEventListener("blur", () => check(el)); el.addEventListener("input", () => { if (el.closest(".field").classList.contains("bad")) check(el); }); });
    form.addEventListener("submit", e => {
      e.preventDefault();
      const res = fields.map(check);
      const msg = $(".form-msg", form);
      if (res.includes(false)) { fields[res.indexOf(false)].focus(); msg.classList.add("hidden"); return; }
      const nameEl = $("[name=name]", form);
      const who = nameEl ? nameEl.value.trim() : "";
      if (form.dataset.validate === "auth") store.set("ip_user", { name: who || $("[name=email]", form).value.split("@")[0] });
      msg.textContent = form.dataset.success.replace("{name}", who || "friend");
      msg.classList.remove("hidden");
      form.reset();
    });
  });

  /* 10. Login tabs + remember user in header */
  const tabs = $(".tabs");
  if (tabs) tabs.addEventListener("click", e => {
    const b = e.target.closest("button");
    if (!b) return;
    $$("button", tabs).forEach(x => x.classList.toggle("on", x === b));
    $$("[data-pane]").forEach(p => p.classList.toggle("hidden", p.dataset.pane !== b.dataset.tab));
  });
  const user = store.get("ip_user"), join = $(".nav .join");
  if (user && join) join.textContent = "Hi, " + user.name.split(" ")[0];
  const logout = $("#logout");
  if (logout) logout.addEventListener("click", () => { store.del("ip_user"); location.reload(); });
});