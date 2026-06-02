import streamlit as st
from youtube_video_analyser import youtube_agent

st.set_page_config(
    page_title="YT Analyser",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Reset & Root ── */
:root {
    --red:     #FF2D2D;
    --red-dim: #991A1A;
    --bg:      #0A0A0A;
    --bg2:     #111111;
    --bg3:     #1A1A1A;
    --border:  #2A2A2A;
    --text:    #E8E4DC;
    --muted:   #666;
    --mono:    'Share Tech Mono', monospace;
    --serif:   'Playfair Display', serif;
    --sans:    'DM Sans', sans-serif;
}

html, body, [data-testid="stAppViewContainer"],
[data-testid="stMain"], .main { 
    background: var(--bg) !important; 
    color: var(--text) !important;
    font-family: var(--sans) !important;
}

/* hide streamlit chrome */
#MainMenu, footer, header, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }

/* ── Scanlines overlay ── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0,0,0,.18) 2px,
        rgba(0,0,0,.18) 4px
    );
    pointer-events: none;
    z-index: 9999;
}

/* ── Main container ── */
.block-container {
    max-width: 780px !important;
    padding: 3rem 1.5rem 5rem !important;
}

/* ── Header ── */
.yt-header {
    text-align: center;
    margin-bottom: 3rem;
    animation: fadeDown .6s ease both;
}
.yt-header .eyebrow {
    font-family: var(--mono);
    font-size: .72rem;
    letter-spacing: .35em;
    color: var(--red);
    text-transform: uppercase;
    margin-bottom: .6rem;
}
.yt-header h1 {
    font-family: var(--serif) !important;
    font-size: clamp(2rem, 6vw, 3.4rem) !important;
    font-weight: 900 !important;
    color: var(--text) !important;
    line-height: 1.05 !important;
    margin: 0 !important;
    letter-spacing: -.02em;
}
.yt-header h1 span { color: var(--red); }
.yt-header .sub {
    font-family: var(--sans);
    font-size: .9rem;
    color: var(--muted);
    margin-top: .8rem;
    font-weight: 300;
}

/* ── Input box ── */
[data-testid="stTextInput"] input {
    background: var(--bg3) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    color: var(--text) !important;
    font-family: var(--mono) !important;
    font-size: .9rem !important;
    padding: .85rem 1.1rem !important;
    transition: border-color .2s, box-shadow .2s !important;
    caret-color: var(--red);
}
[data-testid="stTextInput"] input:focus {
    border-color: var(--red) !important;
    box-shadow: 0 0 0 3px rgba(255,45,45,.12) !important;
    outline: none !important;
}
[data-testid="stTextInput"] input::placeholder { color: var(--muted) !important; }
[data-testid="stTextInput"] label {
    font-family: var(--mono) !important;
    font-size: .72rem !important;
    letter-spacing: .12em !important;
    color: var(--muted) !important;
    text-transform: uppercase;
    margin-bottom: .4rem !important;
}

/* ── Button ── */
[data-testid="stButton"] button {
    width: 100% !important;
    background: var(--red) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 4px !important;
    font-family: var(--mono) !important;
    font-size: .82rem !important;
    letter-spacing: .15em !important;
    text-transform: uppercase !important;
    padding: .85rem 2rem !important;
    cursor: pointer !important;
    transition: background .2s, transform .1s, box-shadow .2s !important;
    position: relative;
    overflow: hidden;
}
[data-testid="stButton"] button:hover {
    background: #FF4444 !important;
    box-shadow: 0 0 28px rgba(255,45,45,.35) !important;
    transform: translateY(-1px) !important;
}
[data-testid="stButton"] button:active { transform: translateY(0) !important; }

/* ── Divider ── */
.yt-divider {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin: 2.5rem 0;
    color: var(--muted);
    font-family: var(--mono);
    font-size: .7rem;
    letter-spacing: .2em;
}
.yt-divider::before, .yt-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

/* ── Spinner override ── */
[data-testid="stSpinner"] {
    display: flex !important;
    justify-content: center !important;
}
[data-testid="stSpinner"] > div {
    border-color: var(--red) transparent transparent transparent !important;
}
.stSpinner p { 
    font-family: var(--mono) !important;
    font-size: .78rem !important;
    color: var(--red) !important;
    letter-spacing: .15em !important;
}

/* ── Spinner card ── */
.decode-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-left: 3px solid var(--red);
    border-radius: 4px;
    padding: 1.5rem 1.8rem;
    margin: 1.5rem 0;
    font-family: var(--mono);
    font-size: .82rem;
    color: var(--muted);
    animation: pulse 2s ease-in-out infinite;
}
.decode-card .blink {
    color: var(--red);
    animation: blink 1s step-end infinite;
}
@keyframes blink { 50% { opacity: 0; } }
@keyframes pulse {
    0%, 100% { border-left-color: var(--red); }
    50%       { border-left-color: var(--red-dim); }
}

/* ── Result container ── */
.result-wrap {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
    animation: fadeUp .5s ease both;
    margin-top: 1.5rem;
}
.result-topbar {
    background: var(--bg3);
    border-bottom: 1px solid var(--border);
    padding: .7rem 1.2rem;
    display: flex;
    align-items: center;
    gap: .6rem;
    font-family: var(--mono);
    font-size: .72rem;
    color: var(--muted);
    letter-spacing: .1em;
}
.result-dot { 
    width: 8px; height: 8px; border-radius: 50%; 
    background: var(--red);
    box-shadow: 0 0 8px var(--red);
}
.result-body {
    padding: 1.8rem 2rem;
}

/* ── Markdown inside result ── */
.result-body h2 {
    font-family: var(--serif) !important;
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    color: var(--text) !important;
    border-bottom: 1px solid var(--border) !important;
    padding-bottom: .4rem !important;
    margin: 1.8rem 0 .8rem !important;
}
.result-body h2:first-child { margin-top: 0 !important; }
.result-body h3 {
    font-family: var(--mono) !important;
    font-size: .82rem !important;
    color: var(--red) !important;
    letter-spacing: .12em !important;
    text-transform: uppercase !important;
    margin: 1.2rem 0 .4rem !important;
}
.result-body p, .result-body li {
    font-family: var(--sans) !important;
    font-size: .93rem !important;
    line-height: 1.75 !important;
    color: #C8C4BC !important;
    font-weight: 300 !important;
}
.result-body ul { padding-left: 1.4rem !important; }
.result-body li { margin-bottom: .3rem !important; }
.result-body strong { color: var(--text) !important; font-weight: 500 !important; }
.result-body code {
    background: var(--bg3) !important;
    color: var(--red) !important;
    font-family: var(--mono) !important;
    font-size: .8rem !important;
    padding: .15em .4em !important;
    border-radius: 3px !important;
}

/* ── Status badge ── */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    background: rgba(255,45,45,.1);
    border: 1px solid rgba(255,45,45,.25);
    border-radius: 3px;
    padding: .25rem .7rem;
    font-family: var(--mono);
    font-size: .7rem;
    color: var(--red);
    letter-spacing: .1em;
    margin-bottom: 1.5rem;
}
.status-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--red);
    animation: blink 1.2s step-end infinite;
}

/* ── Animations ── */
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-18px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ── URL preview chip ── */
.url-chip {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 3px;
    padding: .4rem .8rem;
    font-family: var(--mono);
    font-size: .73rem;
    color: var(--muted);
    margin-bottom: 1rem;
    word-break: break-all;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.url-chip span { color: var(--red); margin-right: .4rem; }
</style>
""", unsafe_allow_html=True)

# ── Header ──
st.markdown("""
<div class="yt-header">
    <div class="eyebrow">// signal intelligence</div>
    <h1>YouTube<br><span>Analyser</span></h1>
    <div class="sub">Paste any YouTube URL. Get deep content intelligence in seconds.</div>
</div>
""", unsafe_allow_html=True)

# ── Agent ──
@st.cache_resource
def get_agent():
    return youtube_agent()

agent = get_agent()

# ── Input ──
video_url = st.text_input(
    "VIDEO URL",
    placeholder="https://www.youtube.com/watch?v=...",
    label_visibility="visible"
)

if video_url:
    st.markdown(f'<div class="url-chip"><span>▶</span>{video_url}</div>', unsafe_allow_html=True)

button = st.button("⬡ &nbsp; DECODE VIDEO")

# ── Analysis ──
if video_url and button:
    st.markdown('<div class="yt-divider">PROCESSING</div>', unsafe_allow_html=True)

    with st.spinner(""):
        st.markdown("""
        <div class="decode-card">
            <span class="blink">█</span>&nbsp; Fetching transcript &amp; metadata...<br>
            <span style="color:#444">── Running content intelligence pipeline</span>
        </div>
        """, unsafe_allow_html=True)

        response = agent.run(f"analyse the video : {video_url}")

    st.markdown('<div class="yt-divider">ANALYSIS COMPLETE</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="status-badge">
        <div class="status-dot"></div> REPORT READY
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="result-wrap"><div class="result-topbar"><div class="result-dot"></div>analysis.md &nbsp;·&nbsp; full report</div><div class="result-body">', unsafe_allow_html=True)
    st.markdown(response.content)
    st.markdown('</div></div>', unsafe_allow_html=True)

elif button and not video_url:
    st.markdown("""
    <div class="decode-card" style="border-left-color:#555; animation:none;">
        <span style="color:#555">⚠</span>&nbsp; No URL detected — paste a YouTube link above.
    </div>
    """, unsafe_allow_html=True)


