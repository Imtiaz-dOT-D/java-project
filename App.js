/* =========================================================
   IRONPULSE - app.js  (login + dashboard)
   NOTE: Abhi data browser ki localStorage mein hai (demo).
   Step 3 mein ye saare DB.* calls asli backend (API) se replace honge,
   aur passwords bcrypt se hash honge. Plain password sirf demo ke liye hai.
   ========================================================= */
"use strict";

/* ---------- Mini "database" (localStorage) ---------- */
const DB = {
  get(key, fallback) {
    try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; }
    catch (e) { return fallback; }
  },
  set(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* ignore */ }
  },
  remove(key) { try { localStorage.removeItem(key); } catch (e) { /* ignore */ } }
};

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const dayKey = d => d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");

/* Demo user pehli baar automatically bana do */
(function seedDemo() {
  const users = DB.get("ip_users", []);
  if (!users.some(u => u.email === "demo@ironpulse.com")) {
    users.push({ name: "Demo Member", email: "demo@ironpulse.com", phone: "03001234567", plan: "Pro", password: "demo1234", joined: new Date(Date.now() - 10 * 86400000).toISOString() });
    DB.set("ip_users", users);
  }
})();

const currentUser = () => {
  const email = DB.get("ip_session", null);
  return DB.get("ip_users", []).find(u => u.email === email) || null;
};

/* =========================================================
   LOGIN PAGE
   ========================================================= */
function initLogin() {
  if (currentUser()) { location.replace("dashboard.html"); return; }

  const msg = $("#authMsg");
  const forms = { login: $("#loginForm"), register: $("#registerForm") };

  /* Tabs */
  $$(".tab").forEach(tab => tab.addEventListener("click", () => {
    $$(".tab").forEach(t => t.classList.toggle("on", t === tab));
    Object.entries(forms).forEach(([name, f]) => f.classList.toggle("hidden", name !== tab.dataset.tab));
    msg.innerHTML = "";
  }));

  /* Validation helpers */
  const fieldsOf = form => $$("input[required], select[required]", form);
  function check(el) {
    if (el.id === "rPass2") el.setCustomValidity(el.value === $("#rPass").value ? "" : "mismatch");
    const ok = el.checkValidity();
    $(".err", el.closest("div")).classList.toggle("hidden", ok);
    el.classList.toggle("!border-red-500", !ok);
    return ok;
  }
  function validate(form) {
    const results = fieldsOf(form).map(check);
    if (results.includes(false)) fieldsOf(form)[results.indexOf(false)].focus();
    return !results.includes(false);
  }
  Object.values(forms).forEach(f => fieldsOf(f).forEach(el => el.addEventListener("blur", () => check(el))));
  const note = (text, ok) => {
    msg.innerHTML = '<p class="rounded-lg p-3 text-sm font-semibold ' + (ok ? "bg-green-500/15 text-green-300" : "bg-red-500/15 text-red-300") + '"></p>';
    msg.firstChild.textContent = text;
  };

  /* Login */
  forms.login.addEventListener("submit", e => {
    e.preventDefault();
    if (!validate(forms.login)) return;
    const email = $("#lEmail").value.trim().toLowerCase();
    const user = DB.get("ip_users", []).find(u => u.email === email && u.password === $("#lPass").value);
    if (!user) { note("Wrong email or password. Please try again.", false); return; }
    DB.set("ip_session", user.email);
    note("Login successful! Redirecting...", true);
    setTimeout(() => location.href = "dashboard.html", 500);
  });

  /* Register */
  forms.register.addEventListener("submit", e => {
    e.preventDefault();
    if (!validate(forms.register)) return;
    const email = $("#rEmail").value.trim().toLowerCase();
    const users = DB.get("ip_users", []);
    if (users.some(u => u.email === email)) { note("This email is already registered. Please login.", false); return; }
    users.push({
      name: $("#rName").value.trim(), email, phone: $("#rPhone").value.trim(),
      plan: $("#rPlan").value, password: $("#rPass").value, joined: new Date().toISOString()
    });
    DB.set("ip_users", users);
    DB.set("ip_session", email);
    note("Account created! Redirecting to your dashboard...", true);
    setTimeout(() => location.href = "dashboard.html", 700);
  });
}

/* =========================================================
   DASHBOARD PAGE
   ========================================================= */
const CLASSES = [
  { id: "c1", name: "Strength Training", when: "Mon 6:00 PM", trainer: "Ali Khan" },
  { id: "c2", name: "HIIT Burn",         when: "Tue 7:00 AM", trainer: "Sara Ahmed" },
  { id: "c3", name: "Spin Cycle",        when: "Wed 6:30 PM", trainer: "Sara Ahmed" },
  { id: "c4", name: "Yoga & Mobility",   when: "Fri 5:30 PM", trainer: "Zain Raza" },
  { id: "c5", name: "HIIT Burn",         when: "Sat 9:00 AM", trainer: "Sara Ahmed" }
];

function initDashboard() {
  const user = currentUser();
  if (!user) { location.replace("login.html"); return; }

  const attKey = "ip_att_" + user.email, bookKey = "ip_book_" + user.email;
  const today = dayKey(new Date());

  /* Toast */
  const toast = $("#toast");
  let tt;
  const say = text => {
    toast.textContent = text; toast.classList.remove("opacity-0");
    clearTimeout(tt); tt = setTimeout(() => toast.classList.add("opacity-0"), 2200);
  };

  /* Header + welcome */
  $("#hdrName").textContent = user.name;
  $("#welcomeName").textContent = user.name.split(" ")[0];
  $("#planName").textContent = user.plan;
  const joined = new Date(user.joined);
  $("#joinedOn").textContent = "Member since " + joined.toLocaleDateString("en-GB", { day: "numeric", month: "short", year: "numeric" });

  /* Membership days left (30 din ki membership) */
  const left = Math.ceil((joined.getTime() + 30 * 86400000 - Date.now()) / 86400000);
  $("#daysLeft").textContent = Math.max(left, 0) + " days";
  $("#daysBar").style.width = Math.min(Math.max(left, 0) / 30 * 100, 100) + "%";
  const note = $("#expiryNote");
  if (left <= 0)      { note.textContent = "Expired. Please renew at the front desk."; note.className = "mt-2 text-sm text-red-400"; }
  else if (left <= 5) { note.textContent = "Expiring soon. Renew to keep your streak."; note.className = "mt-2 text-sm text-yellow-300"; }
  else                { note.textContent = "Your membership is active."; note.className = "mt-2 text-sm text-green-400"; }

  /* Attendance */
  function renderAttendance() {
    const att = DB.get(attKey, []);
    const set = new Set(att);

    /* streak: aaj se peeche ki taraf lagatar din (aaj na hua ho to kal se) */
    let streak = 0, d = new Date();
    if (!set.has(dayKey(d))) d.setDate(d.getDate() - 1);
    while (set.has(dayKey(d))) { streak++; d.setDate(d.getDate() - 1); }
    $("#streak").textContent = streak;
    $("#monthCount").textContent = att.filter(k => k.startsWith(today.slice(0, 7))).length;

    /* 28 din ka calendar */
    const cal = $("#calendar");
    cal.innerHTML = "";
    for (let i = 27; i >= 0; i--) {
      const day = new Date(); day.setDate(day.getDate() - i);
      const k = dayKey(day), hit = set.has(k);
      const cell = document.createElement("div");
      cell.textContent = day.getDate();
      cell.title = k + (hit ? " - attended" : "");
      cell.className = "grid aspect-square place-items-center rounded-md text-xs " +
        (hit ? "bg-neon font-bold text-ink" : "bg-ink2 text-gray-500") + (k === today ? " ring-2 ring-white" : "");
      cal.appendChild(cell);
    }

    const btn = $("#checkinBtn");
    const done = set.has(today);
    btn.disabled = done || left <= 0;
    btn.textContent = done ? "Checked in today \u2713" : "Check in today";
    $("#ciMsg").textContent = left <= 0 ? "Renew your membership to check in." : (done ? "Great work! See you tomorrow." : "Tap when you arrive at the gym.");
  }
  $("#checkinBtn").addEventListener("click", () => {
    const att = DB.get(attKey, []);
    if (!att.includes(today)) { att.push(today); DB.set(attKey, att); say("Checked in. Keep going! \uD83D\uDCAA"); }
    renderAttendance();
  });

  /* Class booking */
  function renderClasses() {
    const booked = DB.get(bookKey, []);
    const list = $("#classList"), mine = $("#myBookings");
    list.innerHTML = ""; mine.innerHTML = "";

    CLASSES.forEach(c => {
      const has = booked.includes(c.id);
      const li = document.createElement("li");
      li.className = "flex items-center justify-between gap-3 py-3";
      li.innerHTML = '<div><p class="font-semibold"></p><p class="text-sm text-gray-400"></p></div><button class="btn-ghost"></button>';
      li.querySelector("p.font-semibold").textContent = c.name;
      li.querySelector("p.text-gray-400").textContent = c.when + " \u00B7 " + c.trainer;
      const b = li.querySelector("button");
      b.textContent = has ? "Booked \u2713" : "Book";
      b.disabled = has;
      if (has) b.classList.add("opacity-50", "cursor-not-allowed");
      b.addEventListener("click", () => {
        booked.push(c.id); DB.set(bookKey, booked); say("Booked: " + c.name); renderClasses();
      });
      list.appendChild(li);
    });

    const mineClasses = CLASSES.filter(c => booked.includes(c.id));
    if (!mineClasses.length) {
      mine.innerHTML = '<li class="text-gray-500">No classes booked yet. Pick one from the list above.</li>';
    }
    mineClasses.forEach(c => {
      const li = document.createElement("li");
      li.className = "flex items-center justify-between gap-3 rounded-lg bg-ink2 px-4 py-3";
      li.innerHTML = '<span></span><button class="text-sm text-red-400 hover:underline">Cancel</button>';
      li.querySelector("span").textContent = c.name + " \u2014 " + c.when;
      li.querySelector("button").addEventListener("click", () => {
        DB.set(bookKey, booked.filter(id => id !== c.id)); say("Booking cancelled"); renderClasses();
      });
      mine.appendChild(li);
    });
  }

  /* Logout */
  $("#logoutBtn").addEventListener("click", () => { DB.remove("ip_session"); location.href = "login.html"; });

  renderAttendance();
  renderClasses();
}

/* Page ke hisaab se sahi function chalao */
document.addEventListener("DOMContentLoaded", () => {
  const page = document.body.dataset.page;
  if (page === "login") initLogin();
  if (page === "dashboard") initDashboard();
});