# ============================================
# MEDICARE AI - COMPLETE FRONTEND
# Streamlit + Animations + Gemini AI
# ============================================

import streamlit as st
import requests
import time

st.set_page_config(
    page_title="MediCare AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BACKEND = "http://127.0.0.1:8000"

for key, val in {
    "logged_in": False,
    "user": None,
    "page": "login"
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif !important; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }

/* ── ANIMATED BACKGROUND ── */
.stApp {
    background: linear-gradient(-45deg, #e3f0ff, #f0f4ff, #e8f5e9, #e3f2fd);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}
@keyframes gradientBG {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── NAVBAR ── */
.navbar {
    background: linear-gradient(90deg, #0D47A1, #1565C0, #1976D2);
    padding: 16px 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 0 0 20px 20px;
    box-shadow: 0 4px 24px rgba(13,71,161,0.25);
    margin-bottom: 28px;
    animation: slideDown 0.5s ease;
}
@keyframes slideDown {
    from { transform: translateY(-60px); opacity: 0; }
    to   { transform: translateY(0);     opacity: 1; }
}
.navbar-brand {
    color: white;
    font-size: 24px;
    font-weight: 800;
    letter-spacing: 0.5px;
}
.navbar-user {
    color: rgba(255,255,255,0.9);
    font-size: 14px;
    font-weight: 500;
}

/* ── CARDS ── */
.card {
    background: white;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.07);
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.8);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    animation: fadeInUp 0.4s ease;
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(21,101,192,0.15);
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
.card-blue {
    background: linear-gradient(135deg, #0D47A1, #1976D2);
    color: white;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 8px 28px rgba(13,71,161,0.3);
    margin-bottom: 20px;
    animation: fadeInUp 0.4s ease;
}
.card-green {
    background: linear-gradient(135deg, #1B5E20, #2E7D32);
    color: white;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 16px;
    animation: fadeInUp 0.5s ease;
}
.card-red {
    background: linear-gradient(135deg, #B71C1C, #C62828);
    color: white;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 16px;
    animation: fadeInUp 0.5s ease;
}
.card-orange {
    background: linear-gradient(135deg, #BF360C, #E64A19);
    color: white;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 16px;
    animation: fadeInUp 0.5s ease;
}
.card-gemini {
    background: linear-gradient(135deg, #4A148C, #6A1B9A, #7B1FA2);
    color: white;
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 20px;
    box-shadow: 0 8px 28px rgba(74,20,140,0.3);
    animation: fadeInUp 0.6s ease;
}

/* ── AUTH FORM ── */
.auth-hero {
    text-align: center;
    padding: 36px 0 16px;
    animation: fadeInUp 0.5s ease;
}
.auth-logo  { font-size: 64px; margin-bottom: 12px; }
.auth-title { font-size: 36px; font-weight: 800; color: #0D47A1; }
.auth-sub   { font-size: 15px; color: #666; margin-top: 6px; }
.form-title { font-size: 24px; font-weight: 800; color: #0D47A1; text-align: center; margin-bottom: 4px; }
.form-sub   { font-size: 14px; color: #666; text-align: center; margin-bottom: 20px; }

/* ── INPUTS ── */
.stTextInput input,
.stNumberInput input {
    border-radius: 12px !important;
    border: 2px solid #e8edf5 !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
    color: #1a1a2e !important;
    background: #fafbff !important;
    transition: border-color 0.2s ease !important;
}
.stTextInput input:focus {
    border-color: #1565C0 !important;
    box-shadow: 0 0 0 3px rgba(21,101,192,0.1) !important;
    background: white !important;
}
.stTextArea textarea {
    border-radius: 12px !important;
    border: 2px solid #e8edf5 !important;
    font-size: 15px !important;
    color: #1a1a2e !important;
    background: #fafbff !important;
}
.stSelectbox > div > div {
    border-radius: 12px !important;
    border: 2px solid #e8edf5 !important;
    color: #1a1a2e !important;
    background: #fafbff !important;
}

/* ── BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg, #0D47A1, #1976D2) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 13px 28px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    width: 100% !important;
    box-shadow: 0 4px 16px rgba(13,71,161,0.3) !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.3px !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #0A3880, #1565C0) !important;
    box-shadow: 0 8px 24px rgba(13,71,161,0.4) !important;
    transform: translateY(-2px) !important;
}

/* ── PAGE TITLES ── */
.page-title {
    font-size: 28px;
    font-weight: 800;
    color: #0D47A1;
    margin-bottom: 4px;
    animation: fadeInUp 0.3s ease;
}
.page-subtitle {
    font-size: 14px;
    color: #777;
    margin-bottom: 24px;
}

/* ── STAT BOX ── */
.stat-box {
    background: white;
    border-radius: 16px;
    padding: 22px;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0,0,0,0.07);
    border-top: 4px solid #1565C0;
    margin-bottom: 16px;
    transition: transform 0.25s ease;
    animation: fadeInUp 0.4s ease;
}
.stat-box:hover { transform: translateY(-4px); }
.stat-number { font-size: 38px; font-weight: 800; color: #1565C0; }
.stat-label  { font-size: 13px; color: #777; font-weight: 600; margin-top: 4px; }

/* ── HISTORY ── */
.history-item {
    background: white;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 14px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    border-left: 5px solid #1565C0;
    transition: transform 0.2s ease;
    animation: fadeInUp 0.4s ease;
}
.history-item:hover { transform: translateX(4px); }

/* ── BADGES ── */
.badge-high   { background:#FFEBEE; color:#B71C1C; border-radius:20px; padding:4px 14px; font-size:12px; font-weight:700; }
.badge-medium { background:#FFF3E0; color:#BF360C; border-radius:20px; padding:4px 14px; font-size:12px; font-weight:700; }
.badge-low    { background:#E8F5E9; color:#1B5E20; border-radius:20px; padding:4px 14px; font-size:12px; font-weight:700; }

/* ── MEDICINE ITEM ── */
.med-item {
    background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
    border-left: 4px solid #1565C0;
    border-radius: 10px;
    padding: 12px 16px;
    margin-bottom: 10px;
    color: #0D47A1;
    font-size: 14px;
    font-weight: 600;
    transition: transform 0.2s ease;
    animation: fadeInUp 0.4s ease;
}
.med-item:hover { transform: translateX(4px); }

/* ── CONFIDENCE BAR ── */
.conf-bar-bg {
    background: #e8edf5;
    border-radius: 8px;
    height: 10px;
    margin-top: 6px;
    overflow: hidden;
}
.conf-bar-fill {
    height: 10px;
    border-radius: 8px;
    background: linear-gradient(90deg, #1565C0, #42A5F5);
    transition: width 1s ease;
}

/* ── DIVIDER ── */
.divider { height: 1px; background: #e8edf2; margin: 20px 0; }

/* ── SPINNER OVERRIDE ── */
.stSpinner > div { border-top-color: #1565C0 !important; }

/* ── PULSE ANIMATION ── */
@keyframes pulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(21,101,192,0.3); }
    50%      { box-shadow: 0 0 0 10px rgba(21,101,192,0); }
}
.pulse { animation: pulse 2s infinite; }

/* ── GEMINI RESPONSE ── */
.gemini-text {
    font-size: 14px;
    color: rgba(255,255,255,0.95);
    line-height: 1.9;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════
def go(page):
    st.session_state.page = page
    st.rerun()

def show_navbar():
    name = st.session_state.user['name'] if st.session_state.logged_in else ""
    st.markdown(f"""
    <div class="navbar">
        <div class="navbar-brand">🏥 MediCare AI</div>
        <div class="navbar-user">{"👤 " + name if name else ""}</div>
    </div>
    """, unsafe_allow_html=True)

def show_nav_tabs():
    c1,c2,c3,c4,c5,c6 = st.columns(6)
    with c1:
        if st.button("🏠 Home",       key="nb1"): go("home")
    with c2:
        if st.button("🔍 Predict",    key="nb2"): go("predict")
    with c3:
        if st.button("📋 History",    key="nb3"): go("history")
    with c4:
        if st.button("📊 Statistics", key="nb4"): go("stats")
    with c5:
        if st.button("👤 Profile",    key="nb5"): go("profile")
    with c6:
        if st.button("🚪 Logout",     key="nb6"): go("logout")

def backend_ok():
    try:
        r = requests.get(f"{BACKEND}/", timeout=2)
        return r.status_code == 200
    except:
        return False

# ═══════════════════════════════════════════════
# PAGE: LOGIN
# ═══════════════════════════════════════════════
def page_login():
    st.markdown("""
    <div class="auth-hero">
        <div class="auth-logo">🏥</div>
        <div class="auth-title">MediCare AI</div>
        <div class="auth-sub">
            AI-powered affordable medicine guidance for everyone
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([1, 1.4, 1])
    with col:
        st.markdown('<div class="card pulse">', unsafe_allow_html=True)
        st.markdown('<div class="form-title">Welcome Back 👋</div>', unsafe_allow_html=True)
        st.markdown('<div class="form-sub">Sign in to continue</div>', unsafe_allow_html=True)

        email    = st.text_input("📧 Email Address", placeholder="you@email.com", key="li_email")
        password = st.text_input("🔒 Password", type="password", placeholder="Enter password", key="li_pass")
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Login to MediCare AI", key="login_btn"):
            if not email.strip() or not password.strip():
                st.error("⚠️ Please enter your email and password.")
            elif not backend_ok():
                st.error("❌ Backend not running! Run: uvicorn backend:app --reload")
            else:
                with st.spinner("Signing you in..."):
                    try:
                        res = requests.post(f"{BACKEND}/login",
                            json={"email": email.strip(),
                                  "password": password.strip()}, timeout=5)
                        if res.status_code == 200:
                            d = res.json()
                            st.session_state.logged_in = True
                            st.session_state.user      = d['user']
                            st.session_state.page      = "home"
                            st.rerun()
                        else:
                            st.error("❌ " + res.json().get("detail", "Invalid credentials."))
                    except Exception as ex:
                        st.error("Connection error: " + str(ex))

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("<div style='text-align:center;color:#777;font-size:14px;'>New to MediCare AI?</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Create Free Account", key="go_signup"):
            go("signup")
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# PAGE: SIGNUP
# ═══════════════════════════════════════════════
def page_signup():
    st.markdown("""
    <div class="auth-hero">
        <div class="auth-logo">🏥</div>
        <div class="auth-title">MediCare AI</div>
        <div class="auth-sub">Create your free account today</div>
    </div>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([1, 1.8, 1])
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="form-title">Create Account 🚀</div>', unsafe_allow_html=True)
        st.markdown('<div class="form-sub">Fill in your details to get started</div>', unsafe_allow_html=True)

        name  = st.text_input("👤 Full Name",     placeholder="Your full name",  key="su_name")
        email = st.text_input("📧 Email Address", placeholder="you@email.com",   key="su_email")

        ca, cb = st.columns(2)
        with ca:
            password = st.text_input("🔒 Password",         type="password", placeholder="Min 6 chars", key="su_pass")
        with cb:
            confirm  = st.text_input("🔒 Confirm Password", type="password", placeholder="Repeat",      key="su_conf")

        cc, cd = st.columns(2)
        with cc:
            age    = st.number_input("🎂 Age", min_value=1, max_value=120, value=20, key="su_age")
        with cd:
            gender = st.selectbox("⚧ Gender", ["Male","Female","Other"], key="su_gender")

        location = st.text_input("📍 City / Location", placeholder="e.g. Bangalore", key="su_loc")
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Create My Account 🎉", key="signup_btn"):
            if not all([name.strip(), email.strip(),
                        password.strip(), confirm.strip(),
                        location.strip()]):
                st.error("⚠️ Please fill in all fields.")
            elif len(password) < 6:
                st.error("⚠️ Password must be at least 6 characters.")
            elif password != confirm:
                st.error("⚠️ Passwords do not match.")
            elif not backend_ok():
                st.error("❌ Backend not running!")
            else:
                with st.spinner("Creating your account..."):
                    try:
                        res = requests.post(f"{BACKEND}/signup", json={
                            "name": name.strip(), "email": email.strip(),
                            "password": password.strip(), "age": int(age),
                            "gender": gender, "location": location.strip()
                        }, timeout=5)
                        if res.status_code == 200:
                            st.success("🎉 Account created! Please login now.")
                            time.sleep(1)
                            go("login")
                        else:
                            st.error("❌ " + res.json().get("detail", "Signup failed."))
                    except Exception as ex:
                        st.error("Connection error: " + str(ex))

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("<div style='text-align:center;color:#777;font-size:14px;'>Already have an account?</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Back to Login", key="go_login"):
            go("login")
        st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# PAGE: HOME
# ═══════════════════════════════════════════════
def page_home():
    show_navbar()
    show_nav_tabs()
    user = st.session_state.user

    st.markdown(f"""
    <div class="card-blue">
        <div style="font-size:26px;font-weight:800;">
            Welcome back, {user['name']}! 👋
        </div>
        <div style="font-size:15px;opacity:0.85;margin-top:8px;">
            {user['gender']} &nbsp;·&nbsp; Age {user['age']}
            &nbsp;·&nbsp; 📍 {user['location']}
        </div>
        <div style="font-size:13px;opacity:0.7;margin-top:6px;">
            Member since {user['joined'][:10]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    for col, icon, title, desc in zip([c1,c2,c3],
        ["🤖","💊","🏥"],
        ["Gemini AI + ML Model","Affordable Medicines","41 Diseases Covered"],
        ["Real-time AI analysis + structured ML prediction",
         "Generic medicines for everyone",
         "Trained on real medical symptom dataset"]
    ):
        with col:
            st.markdown(f"""
            <div class="stat-box">
                <div style="font-size:40px;">{icon}</div>
                <div style="font-size:15px;font-weight:700;
                     color:#1565C0;margin-top:10px;">{title}</div>
                <div style="font-size:13px;color:#777;
                     margin-top:6px;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:18px;font-weight:800;color:#0D47A1;margin-bottom:20px;">📌 How It Works</div>', unsafe_allow_html=True)
    s1,s2,s3,s4 = st.columns(4)
    for col, num, title, desc in zip([s1,s2,s3,s4],
        ["1️⃣","2️⃣","3️⃣","4️⃣"],
        ["Enter Symptoms","Dual AI Analysis","Get Diagnosis","Get Medicines"],
        ["Type your symptoms","ML + Gemini AI both analyze",
         "Disease predicted with confidence","Affordable medicines listed"]
    ):
        with col:
            st.markdown(f"""
            <div style="text-align:center;padding:16px;
                 background:#f8faff;border-radius:16px;">
                <div style="font-size:36px;">{num}</div>
                <div style="font-size:14px;font-weight:700;
                     color:#1565C0;margin:10px 0 6px;">{title}</div>
                <div style="font-size:12px;color:#777;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="border-left:5px solid #D32F2F;">
        <div style="font-size:16px;font-weight:700;
             color:#D32F2F;margin-bottom:8px;">
            ⚠️ Important Disclaimer
        </div>
        <div style="font-size:14px;color:#555;line-height:1.9;">
            This app is for <b>educational purposes only</b> as part of an
            internship project. It is <b>NOT</b> a substitute for professional
            medical advice. Always consult a qualified doctor.
            In emergencies call <b style="color:#D32F2F;">108</b> immediately.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# PAGE: PREDICT
# ═══════════════════════════════════════════════
def page_predict():
    show_navbar()
    show_nav_tabs()

    st.markdown('<div class="page-title">🔍 AI Symptom Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Powered by Machine Learning + Google Gemini AI for accurate, doctor-like analysis</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:16px;font-weight:700;color:#0D47A1;margin-bottom:8px;">📝 Enter Your Symptoms</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-size:13px;color:#777;margin-bottom:10px;">Separate symptoms with spaces. Use underscore for multi-word symptoms e.g. skin_rash, weight_loss, chest_pain</div>', unsafe_allow_html=True)

        symptoms = st.text_area("symptoms", height=120,
            placeholder="e.g.  itching  skin_rash  nodal_skin_eruptions",
            label_visibility="collapsed", key="sym_input")

        st.markdown('<div style="font-size:13px;font-weight:700;color:#0D47A1;margin:14px 0 8px;">⚡ Quick Select:</div>', unsafe_allow_html=True)
        quick = ["fever","headache","nausea","vomiting","fatigue",
                 "cough","itching","skin_rash","chest_pain",
                 "breathlessness","stomach_pain","weight_loss",
                 "back_pain","joint_pain"]
        selected = []
        for row in [quick[:5], quick[5:10], quick[10:]]:
            cols = st.columns(len(row))
            for c, sym in zip(cols, row):
                with c:
                    if st.checkbox(sym, key="q_"+sym):
                        selected.append(sym)

        final = symptoms.strip()
        if selected:
            final = (final + " " + " ".join(selected)).strip()

        if final:
            st.markdown(f"""
            <div style="background:#f0f7ff;border-radius:10px;
                 padding:10px 14px;margin-top:12px;
                 font-size:13px;color:#1565C0;">
                <b>Analyzing:</b> {final}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        btn = st.button("🤖 Analyze with AI & Get Recommendation", key="pred_btn")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div style="font-size:16px;font-weight:700;
                 color:#0D47A1;margin-bottom:12px;">
                💡 Tips for Better Results
            </div>
            <div style="font-size:13px;color:#444;line-height:2.1;">
                ✅ Use exact symptom names<br>
                ✅ Add as many as possible<br>
                ✅ Use underscore for compound words<br>
                ✅ More symptoms = better accuracy<br><br>
                <b style="color:#0D47A1;">Good examples:</b><br>
                <code>itching skin_rash nodal_skin_eruptions</code><br><br>
                <code>fever chills headache nausea vomiting</code><br><br>
                <code>fatigue weight_loss sweating high_fever</code>
            </div>
        </div>
        <div class="card" style="border-left:4px solid #D32F2F;">
            <div style="font-size:15px;font-weight:700;
                 color:#D32F2F;margin-bottom:8px;">
                🚨 Emergency Numbers
            </div>
            <div style="font-size:14px;color:#333;line-height:2.2;">
                🚑 Ambulance: <b>108</b><br>
                🆘 Emergency: <b>112</b><br>
                💊 Jan Aushadhi: <b>1800-180-8080</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if btn:
        if not final.strip():
            st.error("⚠️ Please enter at least one symptom!")
            return

        user = st.session_state.user
        with st.spinner("🤖 Analyzing with ML Model + Gemini AI... please wait"):
            try:
                res = requests.post(f"{BACKEND}/predict", json={
                    "user_id":  user['id'],
                    "username": user['name'],
                    "symptoms": final,
                    "age":      user['age'],
                    "gender":   user['gender']
                }, timeout=30)
                r = res.json()

                st.markdown("---")
                st.markdown('<div style="font-size:24px;font-weight:800;color:#0D47A1;margin-bottom:20px;">📋 AI Prediction Results</div>', unsafe_allow_html=True)

                rc1, rc2 = st.columns([3, 2])

                with rc1:
                    conf = r.get('confidence', 0)
                    top3 = r.get('top3', [])
                    warn = r.get('warning', False)

                    if warn:
                        st.markdown(f"""
                        <div class="card-orange">
                            <div style="font-size:18px;font-weight:700;">
                                ⚠️ Symptoms Too Vague
                            </div>
                            <div style="font-size:14px;margin-top:8px;opacity:0.95;">
                                Confidence: {conf}% — not enough to predict accurately.
                                Please add more specific symptoms.
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="card-blue">
                            <div style="font-size:12px;opacity:0.75;
                                 text-transform:uppercase;letter-spacing:1.5px;">
                                ML Model Prediction
                            </div>
                            <div style="font-size:32px;font-weight:800;
                                 margin:10px 0;">{r['disease']}</div>
                            <div style="font-size:13px;opacity:0.85;">
                                Confidence: {conf}%
                            </div>
                            <div style="background:rgba(255,255,255,0.2);
                                 border-radius:8px;height:8px;
                                 margin-top:10px;overflow:hidden;">
                                <div style="background:white;
                                     width:{min(conf,100)}%;height:8px;
                                     border-radius:8px;"></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                        sev = r['severity']
                        sev_card = ("card-red"    if sev=="High"   else
                                    "card-orange" if sev=="Medium" else "card-green")
                        sev_msg  = ("Consult a doctor immediately — urgent attention needed."
                                    if sev=="High" else
                                    "Monitor carefully. Visit doctor if symptoms worsen."
                                    if sev=="Medium" else
                                    "Can be managed at home. See doctor if no improvement.")

                        st.markdown(f"""
                        <div class="{sev_card}">
                            <div style="font-size:16px;font-weight:700;">
                                Severity: {sev}
                            </div>
                            <div style="font-size:13px;opacity:0.9;
                                 margin-top:6px;">{sev_msg}</div>
                        </div>
                        """, unsafe_allow_html=True)

                    # Top 3 diseases
                    if top3:
                        st.markdown('<div class="card">', unsafe_allow_html=True)
                        st.markdown('<div style="font-size:15px;font-weight:700;color:#0D47A1;margin-bottom:14px;">🔬 Top 3 Possible Conditions</div>', unsafe_allow_html=True)
                        colors = ["#0D47A1","#1976D2","#90CAF9"]
                        for i, t in enumerate(top3):
                            st.markdown(f"""
                            <div style="margin-bottom:14px;">
                                <div style="display:flex;
                                     justify-content:space-between;
                                     font-size:13px;color:#333;
                                     margin-bottom:5px;">
                                    <span style="font-weight:700;
                                          color:{colors[i]};">
                                        {i+1}. {t['disease']}
                                    </span>
                                    <span style="font-weight:700;
                                          color:{colors[i]};">
                                        {t['confidence']}%
                                    </span>
                                </div>
                                <div style="background:#e8edf5;
                                     border-radius:8px;height:10px;
                                     overflow:hidden;">
                                    <div style="background:{colors[i]};
                                         width:{min(t['confidence'],100)}%;
                                         height:10px;border-radius:8px;">
                                    </div>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    # Medical advice
                    if not warn:
                        st.markdown(f"""
                        <div class="card">
                            <div style="font-size:15px;font-weight:700;
                                 color:#0D47A1;margin-bottom:10px;">
                                📋 Medical Advice
                            </div>
                            <div style="font-size:14px;color:#333;
                                 line-height:1.9;">{r['advice']}</div>
                        </div>
                        """, unsafe_allow_html=True)

                with rc2:
                    # Medicines
                    if not warn:
                        st.markdown('<div class="card">', unsafe_allow_html=True)
                        st.markdown('<div style="font-size:15px;font-weight:700;color:#0D47A1;margin-bottom:6px;">💊 Affordable Medicines</div>', unsafe_allow_html=True)
                        st.markdown('<div style="font-size:12px;color:#999;margin-bottom:12px;">Available at Jan Aushadhi & govt hospitals</div>', unsafe_allow_html=True)
                        for med in r['medicines']:
                            st.markdown(f'<div class="med-item">💊 {med}</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                    st.markdown("""
                    <div class="card">
                        <div style="font-size:14px;font-weight:700;
                             color:#2E7D32;margin-bottom:10px;">
                            🏪 Where to Get Free/Cheap Medicines
                        </div>
                        <div style="font-size:13px;color:#333;line-height:2.1;">
                            ✅ Jan Aushadhi Stores<br>
                            ✅ Government Hospitals<br>
                            ✅ Primary Health Centre (PHC)<br>
                            ✅ ASHA Worker<br>
                            ✅ Online: 1mg, PharmEasy
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                # Gemini AI Analysis
                gemini = r.get('gemini_analysis', '')
                if gemini:
                    st.markdown(f"""
                    <div class="card-gemini">
                        <div style="font-size:18px;font-weight:800;
                             margin-bottom:14px;">
                            🤖 Gemini AI Doctor Analysis
                        </div>
                        <div class="gemini-text">{gemini}</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.success("✅ Result saved to your history!")

            except Exception as ex:
                st.error("❌ Could not connect to backend. Error: " + str(ex))

# ═══════════════════════════════════════════════
# PAGE: HISTORY
# ═══════════════════════════════════════════════
def page_history():
    show_navbar()
    show_nav_tabs()
    st.markdown('<div class="page-title">📋 My Prediction History</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">All your past symptom checks and AI predictions</div>', unsafe_allow_html=True)

    user = st.session_state.user
    try:
        res  = requests.get(f"{BACKEND}/history/{user['id']}", timeout=5)
        data = res.json()

        if data['total'] == 0:
            st.info("💡 No predictions yet. Go to Predict page and check your symptoms!")
            return

        total  = data['total']
        high   = sum(1 for p in data['predictions'] if p['severity']=='High')
        medium = sum(1 for p in data['predictions'] if p['severity']=='Medium')
        low    = sum(1 for p in data['predictions'] if p['severity']=='Low')

        c1,c2,c3,c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{total}</div><div class="stat-label">Total Searches</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="stat-box" style="border-top-color:#C62828"><div class="stat-number" style="color:#C62828">{high}</div><div class="stat-label">High Severity</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="stat-box" style="border-top-color:#E64A19"><div class="stat-number" style="color:#E64A19">{medium}</div><div class="stat-label">Medium Severity</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="stat-box" style="border-top-color:#2E7D32"><div class="stat-number" style="color:#2E7D32">{low}</div><div class="stat-label">Low Severity</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        for item in data['predictions']:
            sev    = item['severity']
            border = ("#C62828" if sev=="High" else
                      "#E64A19" if sev=="Medium" else "#2E7D32")
            badge  = "badge-" + sev.lower()
            st.markdown(f"""
            <div class="history-item" style="border-left-color:{border};">
                <div style="display:flex;justify-content:space-between;
                     align-items:center;margin-bottom:10px;">
                    <div style="font-size:17px;font-weight:800;
                         color:#0D47A1;">{item['disease']}</div>
                    <div>
                        <span class="{badge}">{sev}</span>
                        &nbsp;
                        <span style="font-size:12px;color:#aaa;">
                            {item['timestamp']}
                        </span>
                    </div>
                </div>
                <div style="font-size:13px;color:#555;margin-bottom:5px;">
                    <b>Symptoms:</b> {item['symptoms']}
                </div>
                <div style="font-size:13px;color:#555;margin-bottom:5px;">
                    <b>Medicines:</b> {item['medicines']}
                </div>
                <div style="font-size:13px;color:#555;">
                    <b>Advice:</b> {item['advice']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    except Exception as ex:
        st.error("❌ Could not fetch history. Error: " + str(ex))

# ═══════════════════════════════════════════════
# PAGE: STATISTICS
# ═══════════════════════════════════════════════
def page_stats():
    show_navbar()
    show_nav_tabs()
    st.markdown('<div class="page-title">📊 Statistics Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Overview of all predictions made through MediCare AI</div>', unsafe_allow_html=True)

    try:
        import plotly.express as px
        import plotly.graph_objects as go

        res   = requests.get(f"{BACKEND}/stats", timeout=5)
        stats = res.json()
        total = stats['total_predictions']
        sev   = stats['severity_counts']

        c1,c2,c3,c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{total}</div><div class="stat-label">Total Predictions</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="stat-box" style="border-top-color:#C62828"><div class="stat-number" style="color:#C62828">{sev["High"]}</div><div class="stat-label">High Severity</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="stat-box" style="border-top-color:#E64A19"><div class="stat-number" style="color:#E64A19">{sev["Medium"]}</div><div class="stat-label">Medium Severity</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="stat-box" style="border-top-color:#2E7D32"><div class="stat-number" style="color:#2E7D32">{sev["Low"]}</div><div class="stat-label">Low Severity</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div style="font-size:16px;font-weight:700;color:#0D47A1;margin-bottom:12px;">🦠 Top Predicted Diseases</div>', unsafe_allow_html=True)
            if stats['top_diseases']:
                diseases = [d[0] for d in stats['top_diseases']]
                counts   = [d[1] for d in stats['top_diseases']]
                fig = px.bar(x=counts, y=diseases, orientation='h',
                    color=counts, color_continuous_scale='Blues',
                    labels={'x':'Count','y':'Disease'})
                fig.update_layout(
                    paper_bgcolor='white', plot_bgcolor='#f8faff',
                    font=dict(color='#333',size=13),
                    showlegend=False,
                    margin=dict(l=0,r=0,t=0,b=0), height=300)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Make some predictions first!")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div style="font-size:16px;font-weight:700;color:#0D47A1;margin-bottom:12px;">🚦 Severity Distribution</div>', unsafe_allow_html=True)
            fig2 = go.Figure(data=[go.Pie(
                labels=list(sev.keys()),
                values=list(sev.values()),
                hole=0.55,
                marker_colors=['#2E7D32','#E64A19','#C62828'],
                textfont_size=14
            )])
            fig2.update_layout(
                paper_bgcolor='white',
                font=dict(color='#333',size=13),
                margin=dict(l=0,r=0,t=0,b=0), height=300,
                legend=dict(font=dict(color='#333',size=13))
            )
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    except Exception as ex:
        st.error("❌ Could not fetch stats. Error: " + str(ex))

# ═══════════════════════════════════════════════
# PAGE: PROFILE
# ═══════════════════════════════════════════════
def page_profile():
    show_navbar()
    show_nav_tabs()
    st.markdown('<div class="page-title">👤 My Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Your MediCare AI account information</div>', unsafe_allow_html=True)

    user = st.session_state.user
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <div style="font-size:72px;margin-bottom:14px;">👤</div>
            <div style="font-size:22px;font-weight:800;
                 color:#0D47A1;">{user['name']}</div>
            <div style="font-size:14px;color:#777;
                 margin-top:4px;">{user['email']}</div>
            <div style="margin-top:16px;">
                <span class="badge-low"
                      style="font-size:13px;padding:6px 18px;">
                    ✅ Active Member
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:16px;font-weight:700;color:#0D47A1;margin-bottom:16px;">📄 Account Details</div>', unsafe_allow_html=True)
        for label, value in [
            ("Full Name",    user['name']),
            ("Email",        user['email']),
            ("Age",          str(user['age']) + " years"),
            ("Gender",       user['gender']),
            ("Location",     user['location']),
            ("Member Since", user['joined'][:10]),
        ]:
            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;
                 padding:12px 0;border-bottom:1px solid #f0f4f8;">
                <span style="font-size:13px;font-weight:600;
                      color:#999;">{label}</span>
                <span style="font-size:14px;color:#1a1a2e;
                      font-weight:600;">{value}</span>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div style="font-size:16px;font-weight:700;
             color:#0D47A1;margin-bottom:14px;">
            📞 Help & Emergency Contacts
        </div>
        <div style="font-size:14px;color:#333;line-height:2.4;">
            <b>Project:</b> Affordable Medicine Recommender (Internship — Feb to May 2026)<br>
            <b>Domain:</b> Python and AI — Machine Learning<br>
            <b>Tech Stack:</b> Python · FastAPI · SQLite · Scikit-learn · Streamlit · Gemini AI · Plotly<br>
            <b>Dataset:</b> Kaggle — Disease Symptom Description Dataset (4920 records, 41 diseases)<br>
            <b>🚑 Ambulance:</b> 108 &nbsp;&nbsp; <b>🆘 Emergency:</b> 112<br>
            <b>💊 Jan Aushadhi Helpline:</b> 1800-180-8080 (Free medicines)
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# MAIN ROUTER
# ═══════════════════════════════════════════════
def main():
    if st.session_state.page == "logout":
        st.session_state.logged_in = False
        st.session_state.user      = None
        st.session_state.page      = "login"
        st.rerun()

    if not st.session_state.logged_in:
        if st.session_state.page == "signup":
            page_signup()
        else:
            page_login()
    else:
        {
            "home":    page_home,
            "predict": page_predict,
            "history": page_history,
            "stats":   page_stats,
            "profile": page_profile,
        }.get(st.session_state.page, page_home)()

main()