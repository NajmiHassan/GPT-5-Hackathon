import streamlit as st

# =========================
# --------- THEME ---------
# =========================
APP_TITLE = "Grammar Mastery Suite"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Simple educational color scheme
st.markdown(
    """
    <style>
      .app-title {font-size: 2.0rem; font-weight: 800; color: #1e3a8a; margin: .25rem 0 1rem 0;}
      .tense-title {font-size: 1.25rem; font-weight: 800; color: #1e3a8a; margin-top: 4px; margin-bottom: 6px;}
      .subtle-card {background: white; border: 1px solid #e5e7eb; border-radius: 14px; padding: 14px 18px; box-shadow: 0 2px 8px rgba(2,6,23,0.04); margin-bottom: 10px;}
      .instruction {background: #f3f4f6; padding: 10px 12px; border-radius: 12px;}
      .progress-text {font-weight:600;}
    </style>
    """,
    unsafe_allow_html=True,
)

TENSES = [
    "Present Simple", "Present Continuous", "Present Perfect", "Present Perfect Continuous",
    "Past Simple", "Past Continuous", "Past Perfect", "Past Perfect Continuous",
    "Future Simple", "Future Continuous", "Future Perfect", "Future Perfect Continuous",
]

DIFFICULTIES = ["Easy", "Medium", "Hard"]

# =========================
# ---- NAVIGATION BAR -----
# =========================
with st.sidebar:
    st.title("📘 Grammar Mastery Suite")
    nav = st.radio(
        "Navigate:",
        ["Practice Tenses", "MCQs Based Quiz", "Direct/Indirect Speech Practice", "Active/Passive Voice Practice", "Learning Module"],
    )

st.markdown(f'<div class="app-title">{APP_TITLE}</div>', unsafe_allow_html=True)

# =========================
# ---- FRONTEND PAGES ------
# =========================

def render_tense_practice():
    st.markdown('<div class="subtle-card">', unsafe_allow_html=True)
    st.markdown("<b>Configuration Panel</b>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns([1.8, 1, 1, 1])

    with c1:
        sel_tense = st.selectbox("Tense Type", options=TENSES)
    with c2:
        sel_count = st.number_input("How many sentences", min_value=1, max_value=20, value=5, step=1)
    with c3:
        sel_diff = st.selectbox("Difficulty", options=DIFFICULTIES)
    with c4:
        st.write("")
        st.write("")
        start_btn = st.button("Start / Restart", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if start_btn:
        st.info(f"➡️ Call GPT‑5 API here to generate {sel_count} {sel_diff} sentences in {sel_tense}.")

    st.markdown(f'<div class="tense-title">{sel_tense} Practice</div>', unsafe_allow_html=True)
    st.markdown('<div class="instruction">Translate the given Urdu sentence to English.</div>', unsafe_allow_html=True)

    st.text_input("Enter your translation")
    st.button("Submit Answer")
    st.progress(0)
    st.markdown('<span class="progress-text">Progress: 0 / N</span>', unsafe_allow_html=True)
    st.info("Feedback and evaluation will come from GPT‑5 API.")


def render_mcq_quiz():
    st.markdown('<div class="tense-title">MCQs Based Quiz</div>', unsafe_allow_html=True)
    st.markdown('<div class="instruction">Select the best answer. Questions will be served from GPT‑5.</div>', unsafe_allow_html=True)

    st.radio("Your choice:", ["Option A", "Option B", "Option C", "Option D"])
    st.button("Submit")
    st.info("GPT‑5 will provide questions, options, and check answers.")


def render_direct_indirect():
    st.markdown('<div class="tense-title">Direct / Indirect Speech Practice</div>', unsafe_allow_html=True)
    st.text_input("Enter Indirect speech")
    st.button("Submit")
    st.info("➡️ GPT‑5 API will supply direct sentences and evaluate user response.")


def render_voice_practice():
    st.markdown('<div class="tense-title">Active / Passive Voice Practice</div>', unsafe_allow_html=True)
    st.text_input("Enter Passive voice")
    st.button("Submit")
    st.info("➡️ GPT‑5 API will generate active sentences and evaluate transformations.")


def render_learning_module():
    st.markdown('<div class="tense-title">Learning Module</div>', unsafe_allow_html=True)
    st.info("This section can display GPT‑5 generated explanations, rules, and examples dynamically.")

# =========================
# ---- ROUTE RENDERER -----
# =========================
if nav == "Practice Tenses":
    render_tense_practice()
elif nav == "MCQs Based Quiz":
    render_mcq_quiz()
elif nav == "Direct/Indirect Speech Practice":
    render_direct_indirect()
elif nav == "Active/Passive Voice Practice":
    render_voice_practice()
elif nav == "Learning Module":
    render_learning_module()

# =========================
# ---- FOOTER -------------
# =========================
st.markdown("---")
st.caption("Frontend ready. Connect GPT‑5 API calls where info placeholders are shown.")
