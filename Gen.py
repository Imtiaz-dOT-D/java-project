import os
OUT = "/mnt/user-data/outputs/ironpulse-gym/"
NAV = [("index.html","Home"),("about.html","About"),("programs.html","Programs"),("classes.html","Classes"),
       ("trainers.html","Trainers"),("pricing.html","Pricing"),("bmi.html","BMI Tools"),("gallery.html","Gallery"),
       ("blog.html","Blog"),("contact.html","Contact")]

def page(fn, title, desc, body, hero=None):
    nav = "".join('<li><a href="%s"%s>%s</a></li>' % (f, ' aria-current="page"' if f == fn else "", t) for f, t in NAV)
    ph = ('<section class="phero"><div class="wrap"><h1>%s</h1><p>%s</p></div></section>' % hero) if hero else ""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | IRONPULSE Gym</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='20' fill='%230b0d10'/%3E%3Ctext x='50' y='72' font-size='64' text-anchor='middle'%3E%E2%9A%A1%3C/text%3E%3C/svg%3E">
<script src="js/main.js" defer></script>
</head>
<body>
<header class="site-header">
  <div class="wrap bar">
    <a class="logo" href="index.html">&#9889; IRON<span>PULSE</span></a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="nav">&#9776;</button>
    <nav id="nav" class="nav" aria-label="Main navigation">
      <ul>{nav}<li><a class="join" href="login.html">Join Now</a></li></ul>
    </nav>
  </div>
</header>
<main>
{ph}
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="fgrid">
      <div><a class="logo" href="index.html">&#9889; IRON<span>PULSE</span></a><p style="margin-top:.6rem">Train hard. Recover well. Repeat.</p></div>
      <div><h3>Explore</h3><ul><li><a href="programs.html">Programs</a></li><li><a href="classes.html">Class Schedule</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="blog.html">Blog</a></li></ul></div>
      <div><h3>Help</h3><ul><li><a href="faq.html">FAQ</a></li><li><a href="testimonials.html">Success Stories</a></li><li><a href="contact.html">Contact</a></li><li><a href="login.html">Member Login</a></li></ul></div>
      <div><h3>Visit Us</h3><address>Main Boulevard, Karachi<br>info@ironpulse.example<br>+92 300 0000000<br>Mon-Sat 5 AM - 12 AM</address></div>
    </div>
    <p class="copy">&copy; 2026 IronPulse Gym. All rights reserved.</p>
  </div>
</footer>
<button id="toTop" aria-label="Back to top">&uarr;</button>
</body>
</html>
'''
    open(OUT + fn, "w", encoding="utf-8").write(html)

def cards(items):
    return "".join('<article class="card"><span class="ico" aria-hidden="true">%s</span><h3>%s</h3><p>%s</p></article>' % i for i in items)

CTA = '<section><div class="wrap"><div class="cta"><h2>Ready to <span>start?</span></h2><p>Your first week is free. No credit card needed.</p><a class="btn btn-n" href="login.html">Claim Free Week</a></div></div></section>'

# ---------------- 1. HOME ----------------
page("index.html", "Home", "IronPulse Gym: strength, HIIT, cardio and yoga with certified trainers in Karachi.", f'''
<section class="hero"><div class="wrap">
  <p class="kicker">NO EXCUSES. JUST RESULTS.</p>
  <h1>Build your <span>strongest</span> self</h1>
  <p class="lead">Premium equipment, certified trainers and programs made for every level. Your first week is on us.</p>
  <p><a class="btn btn-n" href="login.html">Start Free Week</a> <a class="btn btn-o" href="programs.html">Explore Programs</a></p>
</div></section>
<section class="alt"><div class="wrap grid">
  <div class="stat"><b data-count="2500" data-suffix="+">0</b>Active Members</div>
  <div class="stat"><b data-count="30" data-suffix="+">0</b>Expert Trainers</div>
  <div class="stat"><b data-count="120" data-suffix="+">0</b>Weekly Classes</div>
  <div class="stat"><b data-count="12">0</b>Years Strong</div>
</div></section>
<section><div class="wrap"><h2>Why <span>IronPulse</span></h2><div class="grid">
{cards([("&#127942;","Premium Equipment","Modern machines, free weights and a dedicated functional zone."),("&#128170;","Certified Coaches","Trainers with real certifications and years of experience."),("&#9200;","Open Long Hours","Train from 5 AM to midnight, six days a week."),("&#128737;&#65039;","Clean &amp; Safe","Daily sanitising, air-conditioned floors and clean locker rooms.")])}
</div></div></section>
<section class="alt"><div class="wrap"><h2>Popular <span>programs</span></h2><div class="grid">
{cards([("&#127947;&#65039;","Strength Training","Build muscle with progressive overload."),("&#128293;","HIIT Burn","45-minute sessions that torch calories."),("&#129496;","Yoga &amp; Mobility","Flexibility, posture and recovery.")])}
</div><p class="center" style="margin-top:1.5rem"><a class="btn btn-o" href="programs.html">See all programs</a></p></div></section>
{CTA}''')

# ---------------- 2. ABOUT ----------------
page("about.html", "About Us", "Learn the story, mission and values behind IronPulse Gym.", f'''
<section><div class="wrap grid-2">
  <div><h2>Our <span>story</span></h2><p>IronPulse started in 2014 as a small 800 sq ft studio with six machines and one big idea: fitness should feel welcoming, not intimidating.</p><p>Today we are a full-size gym with more than 2,500 members, 30 coaches and over 120 classes every week, but the idea has not changed.</p></div>
  <div class="panel"><h3>Mission</h3><p>To help every member become stronger, healthier and more confident through expert guidance.</p><h3>Vision</h3><p>To be the most trusted community gym in Karachi.</p></div>
</div></section>
<section class="alt"><div class="wrap"><h2>Our <span>values</span></h2><div class="grid">
{cards([("&#129309;","Community","We celebrate every member, from first-timers to athletes."),("&#128201;","Progress","We track results and adjust your plan every month."),("&#128154;","Wellbeing","Strength and mental health go hand in hand.")])}
</div></div></section>
<section><div class="wrap"><h2>Our <span>facilities</span></h2><ul class="perks"><li>6,000 sq ft training floor</li><li>Separate cardio and functional zones</li><li>Yoga and group-class studio</li><li>Locker rooms with showers</li><li>Juice bar and supplement counter</li><li>Free parking</li></ul></div></section>
{CTA}''', ("About <span style='color:#c6ff3d'>IronPulse</span>", "More than a gym. A community built around real results."))

# ---------------- 3. PROGRAMS ----------------
progs = [("strength","&#127947;&#65039;","Strength Training","Barbells, dumbbells and machines with progressive overload.","All levels","60 min"),
 ("cardio","&#128293;","HIIT Burn","High intensity intervals that burn fat fast.","Intermediate","45 min"),
 ("cardio","&#128692;","Spin Cycle","Music-driven indoor cycling for stamina.","All levels","45 min"),
 ("mind","&#129496;","Yoga &amp; Mobility","Stretching, breathing and recovery work.","Beginner","60 min"),
 ("strength","&#129354;","Boxing Fit","Pad work and bag drills for power and speed.","Intermediate","50 min"),
 ("strength","&#9889;","CrossFit Basics","Functional movements, kettlebells and conditioning.","Advanced","60 min")]
pc = "".join('<article class="card prog" data-cat="%s"><span class="ico">%s</span><h3>%s</h3><p>%s</p><span class="tag">%s</span><span class="tag">%s</span></article>' % p for p in progs)
page("programs.html", "Programs", "Strength, HIIT, spin, yoga, boxing and CrossFit programs.", f'''
<section><div class="wrap">
<div class="chips" data-target=".prog"><button class="on" data-filter="all">All</button><button data-filter="strength">Strength</button><button data-filter="cardio">Cardio</button><button data-filter="mind">Mind &amp; Body</button></div>
<div class="grid">{pc}</div></div></section>{CTA}''', ("Our <span style='color:#c6ff3d'>Programs</span>", "Pick a program that matches your goal and fitness level."))

# ---------------- 4. CLASSES ----------------
rows = [("mon","Monday","Strength Training","6:00 PM","Ali Khan"),("tue","Tuesday","HIIT Burn","7:00 AM","Sara Ahmed"),("wed","Wednesday","Spin Cycle","6:30 PM","Sara Ahmed"),
 ("thu","Thursday","Boxing Fit","7:00 PM","Bilal Raza"),("fri","Friday","Yoga &amp; Mobility","5:30 PM","Zain Raza"),("sat","Saturday","HIIT Burn","9:00 AM","Sara Ahmed"),("sat","Saturday","CrossFit Basics","11:00 AM","Bilal Raza")]
tr = "".join('<tr class="cls" data-cat="%s"><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in rows)
page("classes.html", "Class Schedule", "Weekly class timetable at IronPulse Gym.", f'''
<section><div class="wrap">
<div class="chips" data-target=".cls"><button class="on" data-filter="all">All days</button><button data-filter="mon">Mon</button><button data-filter="tue">Tue</button><button data-filter="wed">Wed</button><button data-filter="thu">Thu</button><button data-filter="fri">Fri</button><button data-filter="sat">Sat</button></div>
<div class="tscroll"><table><caption>Weekly timetable. Sunday is open gym (8 AM - 8 PM).</caption><thead><tr><th>Day</th><th>Class</th><th>Time</th><th>Trainer</th></tr></thead><tbody>{tr}</tbody></table></div>
<p style="margin-top:1rem">Book your spot at the front desk or call us. Classes are included in Pro and Elite plans.</p></div></section>{CTA}''',
 ("Class <span style='color:#c6ff3d'>Schedule</span>", "Find the class that fits your day."))

# ---------------- 5. TRAINERS ----------------
tr_ = [("AK","Ali Khan","Strength Coach","8 years in powerlifting and muscle building. NASM certified."),("SA","Sara Ahmed","HIIT &amp; Cardio","Fat-loss specialist and ACE certified group instructor."),
 ("ZR","Zain Raza","Yoga &amp; Mobility","Helps members recover faster and move better every day."),("BR","Bilal Raza","Boxing &amp; CrossFit","Former amateur boxer focused on speed and conditioning.")]
tc = "".join('<article class="card center"><div class="avatar">%s</div><h3>%s</h3><p class="kicker" style="letter-spacing:.1em">%s</p><p>%s</p></article>' % t for t in tr_)
page("trainers.html", "Trainers", "Meet the certified coaches at IronPulse Gym.", f'<section><div class="wrap"><div class="grid">{tc}</div></div></section>{CTA}',
 ("Meet the <span style='color:#c6ff3d'>Trainers</span>", "Certified, friendly and focused on your progress."))

# ---------------- 6. PRICING ----------------
def plan(name, m, y, perks, feat=False, extra=""):
    li = "".join("<li>%s</li>" % p for p in perks)
    return f'<article class="card{" feat" if feat else ""}">{extra}<h3>{name}</h3><p class="price">$<span data-m="{m}" data-y="{y}">{m}</span><small class="per">/month</small></p><ul class="perks">{li}</ul><a class="btn {"btn-n" if feat else "btn-o"}" href="login.html">Choose {name}</a></article>'
page("pricing.html", "Pricing", "Simple monthly and yearly membership plans.", f'''
<section><div class="wrap center">
<label class="switch"><span>Monthly</span><input type="checkbox" id="billing"><i></i><span>Yearly (save 20%)</span></label>
<div class="grid" style="text-align:left">
{plan("Basic",25,240,["Gym floor access","Locker room","1 fitness assessment"])}
{plan("Pro",45,432,["Everything in Basic","All group classes","Monthly body scan"],True,'<span class="tag" style="background:#ffd24a;color:#0b0d10">MOST POPULAR</span>')}
{plan("Elite",79,758,["Everything in Pro","4 personal training sessions","Custom diet plan"])}
</div>
<div class="tscroll" style="margin-top:2.5rem;text-align:left"><table><caption>Plan comparison</caption><thead><tr><th>Feature</th><th>Basic</th><th>Pro</th><th>Elite</th></tr></thead><tbody>
<tr><td>Gym access</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Group classes</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Personal training</td><td>No</td><td>No</td><td>4 / month</td></tr><tr><td>Diet plan</td><td>No</td><td>No</td><td>Yes</td></tr></tbody></table></div>
</div></section>''', ("Membership <span style='color:#c6ff3d'>Plans</span>", "No joining fee this month. Cancel or freeze anytime."))

# ---------------- 7. BMI ----------------
page("bmi.html", "BMI & Calorie Tools", "Free BMI and daily calorie calculators.", '''
<section><div class="wrap grid-2">
<div class="panel"><h2>BMI <span>calculator</span></h2>
<form id="bmiForm" novalidate><div class="field"><label for="bw">Weight (kg)</label><input id="bw" type="number" min="20" max="300"></div>
<div class="field"><label for="bh">Height (cm)</label><input id="bh" type="number" min="100" max="250"></div>
<button class="btn btn-n" type="submit">Calculate BMI</button></form><div class="result" id="bmiOut" role="status">Enter your details to see your BMI.</div></div>
<div class="panel"><h2>Calorie <span>calculator</span></h2>
<form id="calForm" novalidate><div class="field"><label for="cg">Gender</label><select id="cg"><option value="m">Male</option><option value="f">Female</option></select></div>
<div class="field"><label for="ca">Age</label><input id="ca" type="number" min="12" max="90"></div>
<div class="field"><label for="cw">Weight (kg)</label><input id="cw" type="number"></div>
<div class="field"><label for="ch">Height (cm)</label><input id="ch" type="number"></div>
<div class="field"><label for="cact">Activity</label><select id="cact"><option value="1.2">Little or no exercise</option><option value="1.55" selected>Exercise 3-5 days a week</option><option value="1.75">Hard exercise 6-7 days</option></select></div>
<div class="field"><label for="cgoal">Goal</label><select id="cgoal"><option value="-500">Lose weight</option><option value="0" selected>Maintain</option><option value="300">Build muscle</option></select></div>
<button class="btn btn-n" type="submit">Calculate Calories</button></form><div class="result" id="calOut" role="status">Your daily calories will appear here.</div></div>
</div></section>
<section class="alt"><div class="wrap"><div class="tscroll"><table><caption>BMI categories (adults)</caption><thead><tr><th>BMI</th><th>Category</th></tr></thead><tbody><tr><td>Below 18.5</td><td>Underweight</td></tr><tr><td>18.5 - 24.9</td><td>Healthy</td></tr><tr><td>25 - 29.9</td><td>Overweight</td></tr><tr><td>30 and above</td><td>Obese</td></tr></tbody></table></div><p style="margin-top:1rem">These tools give a general estimate only. Ask our trainers for a full assessment.</p></div></section>''',
 ("BMI &amp; Calorie <span style='color:#c6ff3d'>Tools</span>", "Know your numbers before you start."))

# ---------------- 8. GALLERY ----------------
tiles = [("Free Weights","#4a6b00","#0b0d10"),("Cardio Zone","#0e5a7a","#0b0d10"),("HIIT Studio","#8a2d12","#0b0d10"),("Yoga Room","#5a2a7a","#0b0d10"),("Boxing Corner","#7a1f2b","#0b0d10"),("Locker Rooms","#7a5a0e","#0b0d10"),("Juice Bar","#0e6a5a","#0b0d10"),("Functional Zone","#2a3a7a","#0b0d10")]
gt = "".join('<button class="tile" style="--c1:%s;--c2:%s" data-caption="%s: a clean, well-equipped area at IronPulse. (Replace with a real photo.)">%s</button>' % (a, b, n, n) for n, a, b in tiles)
page("gallery.html", "Gallery", "Photos of the IronPulse Gym facilities.", f'''
<section><div class="wrap"><div class="grid">{gt}</div><p style="margin-top:1rem">Click a tile to open it. Real photos can replace these tiles later.</p></div></section>
<dialog id="lb"><h2 id="lbTitle"></h2><p id="lbText"></p><button class="btn btn-n" id="lbClose">Close</button></dialog>''',
 ("Inside the <span style='color:#c6ff3d'>Gym</span>", "Take a look around our training floors and studios."))

# ---------------- 9. BLOG ----------------
posts = [("Nutrition","12 Mar 2026","How much protein do you really need?","Most active adults need 1.2 to 2.0 g of protein per kg of body weight daily. Spread it across meals and pair it with strength training."),
 ("Training","28 Feb 2026","Beginner full-body workout plan","Train three days a week: squat, push, pull, hinge and core. Start light, learn the form and add weight slowly each week."),
 ("Recovery","10 Feb 2026","Why sleep is your best supplement","Muscles repair while you sleep. Aim for 7 to 9 hours, keep a fixed bedtime and avoid screens before bed."),
 ("Mindset","22 Jan 2026","How to stay consistent after week three","Plan your sessions like appointments, track progress and find a training partner. Motivation fades, habits stay.")]
pp = "".join('<article class="card"><span class="tag">%s</span> <time>%s</time><h3 style="margin-top:.6rem">%s</h3><details><summary>Read more</summary><p>%s</p></details></article>' % p for p in posts)
page("blog.html", "Blog", "Fitness, nutrition and recovery tips from IronPulse coaches.", f'<section><div class="wrap"><div class="grid">{pp}</div></div></section>{CTA}',
 ("Fitness <span style='color:#c6ff3d'>Blog</span>", "Tips from our coaches to help you train smarter."))

# ---------------- 10. FAQ ----------------
faqs = [("Is there a joining fee?","Admission is free during our current offer. Monthly fees depend on your plan."),("Do you have ladies-only timings?","Yes. We have ladies-only slots and a female trainer. Ask at the front desk for the timetable."),
 ("I am a beginner. Can I join?","Absolutely. Every new member gets a free fitness assessment and a beginner plan."),("Can I freeze my membership?","Pro and Elite members can freeze their plan for up to 30 days per year."),
 ("What should I bring?","A towel, water bottle and clean indoor shoes. Lockers are available."),("How can I pay?","Cash, bank transfer, JazzCash or Easypaisa."),
 ("Do you offer personal training?","Yes. Elite includes 4 sessions a month, and extra sessions can be added to any plan."),("Is parking available?","Yes, free parking for members.")]
fq = "".join('<details class="faq-item"><summary>%s</summary><p>%s</p></details>' % f for f in faqs)
page("faq.html", "FAQ", "Answers to common questions about IronPulse Gym.", f'''
<section><div class="wrap" style="max-width:780px"><div class="field"><label for="faqSearch">Search questions</label><input id="faqSearch" type="search" placeholder="Type e.g. parking, fee, freeze..."></div>
{fq}<p id="faqEmpty" class="hidden">No question matches your search. Please <a href="contact.html">contact us</a>.</p></div></section>''',
 ("Frequently Asked <span style='color:#c6ff3d'>Questions</span>", "Quick answers before you join."))

# ---------------- 11. TESTIMONIALS ----------------
ts = [("Hamza","Pro Member","Lost 12 kg in four months. The trainers really care about progress."),("Ayesha","Basic Member","Clean gym, friendly people and amazing classes. Best decision this year."),
 ("Bilal","Elite Member","The personal plan helped me finally build muscle the right way."),("Fatima","Pro Member","The yoga and HIIT mix fixed my back pain and my stamina."),
 ("Usman","Basic Member","Great equipment and never too crowded. Worth every rupee."),("Hira","Elite Member","My coach adjusts my diet every month. I feel stronger than ever.")]
tt = "".join('<article class="card"><p class="stars" aria-label="5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</p><p>&ldquo;%s&rdquo;</p><h3>%s</h3><span class="tag">%s</span></article>' % (c, n, r) for n, r, c in ts)
page("testimonials.html", "Success Stories", "Real member stories from IronPulse Gym.", f'<section><div class="wrap"><div class="grid">{tt}</div></div></section>{CTA}',
 ("Member <span style='color:#c6ff3d'>Stories</span>", "Real people. Real progress."))

# ---------------- 12. CONTACT ----------------
page("contact.html", "Contact", "Contact IronPulse Gym: address, phone, timings and enquiry form.", '''
<section><div class="wrap grid-2">
<div class="panel"><h2>Send a <span>message</span></h2>
<form data-validate="contact" data-success="Thank you, {name}! We received your message and will reply soon." novalidate>
<div class="field"><label for="name">Full name</label><input id="name" name="name" type="text" required minlength="3"><p class="err">Please enter your name (min 3 letters).</p></div>
<div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required><p class="err">Enter a valid email address.</p></div>
<div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" required pattern="[0-9+\\- ]{10,15}"><p class="err">Enter a valid phone number.</p></div>
<div class="field"><label for="topic">Topic</label><select id="topic" required><option value="">Choose...</option><option>Membership</option><option>Personal training</option><option>Other</option></select><p class="err">Please choose a topic.</p></div>
<div class="field"><label for="msg">Message</label><textarea id="msg" required minlength="10" maxlength="500"></textarea><p class="err">Message must be at least 10 characters.</p></div>
<button class="btn btn-n" type="submit">Send Message</button><p class="form-msg hidden" role="status"></p></form></div>
<div><div class="panel"><h3>Visit us</h3><address style="font-style:normal;color:#9aa7b4;line-height:1.9">Main Boulevard, Karachi, Pakistan<br>Phone: +92 300 0000000<br>Email: info@ironpulse.example</address>
<div class="tscroll" style="margin-top:1rem"><table style="min-width:0"><caption>Opening hours</caption><tbody><tr><td>Mon - Sat</td><td>5 AM - 12 AM</td></tr><tr><td>Sunday</td><td>8 AM - 8 PM</td></tr></tbody></table></div></div>
<iframe title="Gym location map" loading="lazy" style="width:100%;height:260px;border:1px solid #252d38;border-radius:14px;margin-top:1.2rem" src="https://www.google.com/maps?q=Karachi,Pakistan&output=embed"></iframe></div>
</div></section>''', ("Contact <span style='color:#c6ff3d'>Us</span>", "Questions? We usually reply within a few hours."))

# ---------------- 13. LOGIN ----------------
page("login.html", "Member Login", "Login or create your IronPulse member account.", '''
<section><div class="wrap" style="max-width:480px"><div class="panel">
<div class="tabs"><button class="on" data-tab="login">Login</button><button data-tab="register">Register</button></div>
<form data-pane="login" data-validate="auth" data-success="Welcome back, {name}! (Front-end demo: no real account is checked.)" novalidate>
<div class="field"><label for="le">Email</label><input id="le" name="email" type="email" required><p class="err">Enter a valid email address.</p></div>
<div class="field"><label for="lp">Password</label><input id="lp" name="password" type="password" required minlength="8"><p class="err">Password must be at least 8 characters.</p></div>
<button class="btn btn-n" type="submit">Login</button><p class="form-msg hidden" role="status"></p></form>
<form data-pane="register" class="hidden" data-validate="auth" data-success="Account created, {name}! Welcome to IronPulse. (Front-end demo)" novalidate>
<div class="field"><label for="rn">Full name</label><input id="rn" name="name" type="text" required minlength="3"><p class="err">Please enter your name.</p></div>
<div class="field"><label for="re">Email</label><input id="re" name="email" type="email" required><p class="err">Enter a valid email address.</p></div>
<div class="field"><label for="rp">Password</label><input id="rp" name="password" type="password" required minlength="8"><p class="err">Password must be at least 8 characters.</p></div>
<div class="field"><label><input type="checkbox" required> I agree to the gym rules and terms</label><p class="err">You must agree to continue.</p></div>
<button class="btn btn-n" type="submit">Create Account</button><p class="form-msg hidden" role="status"></p></form>
<p style="margin:1rem 0 0;font-size:.85rem">This is a front-end demo. Data is not sent to any server. <a href="#" id="logout">Log out</a></p>
</div></div></section>''', ("Member <span style='color:#c6ff3d'>Area</span>", "Login or join IronPulse in a minute."))

# ---------------- 14. 404 ----------------
page("404.html", "Page not found", "This page does not exist.", '<section><div class="wrap center"><h1>4<span>0</span>4</h1><p class="lead">This page skipped leg day and disappeared.</p><a class="btn btn-n" href="index.html">Back to Home</a></div></section>')

open(OUT + "README.md", "w", encoding="utf-8").write("""# IronPulse Gym Website

A 14-page, fully responsive gym website built with **HTML5, CSS3 and vanilla JavaScript** (no frameworks).

## Pages
Home, About, Programs, Class Schedule, Trainers, Pricing, BMI & Calorie Tools, Gallery, Blog, FAQ, Success Stories, Contact, Member Login, 404.

## Features
- Responsive layout (Flexbox, Grid, media queries) and mobile menu
- Program and class filters, pricing toggle, FAQ search, gallery lightbox
- BMI and daily calorie calculators
- Form validation (contact, login, register)
- Animated counters, back-to-top button

## Run locally
Open `index.html` in a browser.

## Live website
https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/
""")
print("done")