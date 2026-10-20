import pandas as pd
import plotly.express as px
import streamlit as st
from datetime import timedelta

st.set_page_config(
    page_title='Healthcare Dashboard',
    layout='wide',
    page_icon="🏥"
)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap');

/* ================================
   GLOBAL THEME
================================ */
:root {
    --bg: #030712;
    --surface: #0b1220;
    --surface-light: #111c2e;
    --teal: #00d4aa;
    --sky: #38bdf8;
    --violet: #8b5cf6;
    --rose: #fb7185;
    --text: #e5edf7;
    --muted: #94a3b8;
    --border: rgba(148, 163, 184, 0.12);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--text);
}

.stApp {
    background-color: var(--bg);
    background-image:
        radial-gradient(ellipse at 10% 10%, rgba(0, 212, 170, 0.12), transparent 35%),
        radial-gradient(ellipse at 90% 15%, rgba(56, 189, 248, 0.12), transparent 35%),
        radial-gradient(ellipse at 55% 90%, rgba(139, 92, 246, 0.12), transparent 40%);
    background-size: 200% 200%;
    animation: meshMove 18s ease-in-out infinite alternate;
}

@keyframes meshMove {
    0% {
        background-position: 0% 0%, 100% 0%, 50% 100%;
    }
    50% {
        background-position: 30% 40%, 70% 30%, 40% 70%;
    }
    100% {
        background-position: 60% 20%, 40% 60%, 70% 40%;
    }
}

/* ================================
   TYPOGRAPHY
================================ */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Syne', sans-serif !important;
    color: #f8fafc !important;
    font-weight: 700 !important;
    letter-spacing: -0.035em;
}

h1 {
    font-size: clamp(2rem, 4vw, 3.2rem) !important;
    background: linear-gradient(110deg, #ffffff, var(--teal), var(--sky));
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

p, label, span, li {
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stCaptionContainer"] {
    color: var(--muted);
}

/* ================================
   MAIN CONTENT
================================ */
[data-testid="stAppViewContainer"] {
    background: transparent;
}

[data-testid="stHeader"] {
    background: rgba(3, 7, 18, 0.75);
    backdrop-filter: blur(14px);
}

[data-testid="stMain"] {
    background: transparent;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1440px;
    animation: fadeUp 0.8s ease-out both;
}

/* ================================
   FADE-UP ENTRANCE ANIMATION
================================ */
@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(22px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

[data-testid="stVerticalBlock"] > div {
    animation: fadeUp 0.65s ease-out both;
}

/* ================================
   METRIC CARDS
================================ */
[data-testid="stMetric"] {
    position: relative;
    background: linear-gradient(
        145deg,
        rgba(17, 28, 46, 0.88),
        rgba(7, 14, 27, 0.88)
    );
    border: 1px solid rgba(148, 163, 184, 0.13);
    border-radius: 18px;
    padding: 22px 24px;
    overflow: hidden;
    backdrop-filter: blur(18px);
    box-shadow:
        0 8px 32px rgba(0, 0, 0, 0.18),
        inset 0 1px 0 rgba(255, 255, 255, 0.025);
    transition:
        transform 0.3s ease,
        border-color 0.3s ease,
        box-shadow 0.3s ease;
}

[data-testid="stMetric"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 10%;
    right: 10%;
    height: 2px;
    background: linear-gradient(
        90deg,
        transparent,
        var(--teal),
        var(--sky),
        transparent
    );
    box-shadow: 0 0 18px rgba(0, 212, 170, 0.65);
}

[data-testid="stMetric"]:hover {
    transform: translateY(-6px);
    border-color: rgba(0, 212, 170, 0.35);
    box-shadow:
        0 16px 38px rgba(0, 0, 0, 0.28),
        0 0 24px rgba(0, 212, 170, 0.08);
}

[data-testid="stMetricLabel"] {
    color: var(--muted) !important;
    font-size: 0.9rem;
    font-weight: 500;
}

[data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 1.55rem !important;
    font-weight: 800 !important;
}

[data-testid="stMetricDelta"] {
    font-weight: 600;
}

/* ================================
   SIDEBAR
================================ */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #080f1d 0%,
        #070c18 55%,
        #0a1020 100%
    );
    border-right: 1px solid rgba(0, 212, 170, 0.12);
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
    color: #f1f5f9 !important;
}

[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    gap: 0.8rem;
}

/* ================================
   SIDEBAR EXPANDERS
================================ */
[data-testid="stSidebar"] [data-testid="stExpander"] {
    background: rgba(17, 28, 46, 0.58);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

[data-testid="stSidebar"] [data-testid="stExpander"]:hover {
    border-color: rgba(0, 212, 170, 0.38);
    box-shadow: 0 0 18px rgba(0, 212, 170, 0.07);
}

[data-testid="stSidebar"] [data-testid="stExpander"] summary {
    color: var(--text);
    font-weight: 600;
    padding: 12px;
}

[data-testid="stSidebar"] [data-testid="stExpander"] summary:hover {
    color: var(--teal);
}

[data-testid="stSidebar"] [data-testid="stExpanderDetails"] {
    background: rgba(3, 7, 18, 0.35);
}

/* ================================
   INPUTS
================================ */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
.stDateInput input,
.stTimeInput input,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    background: rgba(8, 15, 29, 0.9) !important;
    color: var(--text) !important;
    border: 1px solid rgba(148, 163, 184, 0.2) !important;
    border-radius: 12px !important;
    caret-color: var(--teal);
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus,
.stDateInput input:focus,
.stTimeInput input:focus,
[data-baseweb="input"]:focus-within,
[data-baseweb="textarea"]:focus-within {
    border-color: var(--teal) !important;
    box-shadow: 0 0 0 2px rgba(0, 212, 170, 0.15),
                0 0 16px rgba(0, 212, 170, 0.08) !important;
}

/* Select boxes */
[data-baseweb="select"] > div {
    background: rgba(8, 15, 29, 0.95) !important;
    color: var(--text) !important;
    border-color: rgba(148, 163, 184, 0.2) !important;
    border-radius: 12px !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

[data-baseweb="select"] > div:focus-within {
    border-color: var(--teal) !important;
    box-shadow: 0 0 0 2px rgba(0, 212, 170, 0.15) !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"],
[data-baseweb="listbox"] {
    background: #0b1220 !important;
    border: 1px solid rgba(0, 212, 170, 0.2) !important;
    border-radius: 12px !important;
}

[role="option"] {
    background: transparent !important;
    color: var(--text) !important;
    transition: background 0.2s ease;
}

[role="option"]:hover,
[aria-selected="true"] {
    background: rgba(0, 212, 170, 0.12) !important;
    color: var(--teal) !important;
}

/* ================================
   MULTISELECT CHIPS
================================ */
[data-baseweb="tag"] {
    background: rgba(0, 212, 170, 0.14) !important;
    color: var(--teal) !important;
    border: 1px solid rgba(0, 212, 170, 0.32) !important;
    border-radius: 8px !important;
}

[data-baseweb="tag"] span {
    color: var(--teal) !important;
}

[data-baseweb="tag"] svg {
    fill: var(--teal) !important;
}

[data-baseweb="tag"]:hover {
    background: rgba(0, 212, 170, 0.23) !important;
}

/* ================================
   SLIDERS
================================ */
[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
    background: var(--teal) !important;
    border-color: var(--teal) !important;
    box-shadow: 0 0 12px rgba(0, 212, 170, 0.45);
}

[data-testid="stSlider"] [data-baseweb="slider"] > div > div {
    background: linear-gradient(90deg, var(--teal), var(--sky)) !important;
}

[data-testid="stSlider"] [data-testid="stTickBar"] {
    background: rgba(148, 163, 184, 0.2);
}

/* ================================
   CHECKBOXES & RADIO BUTTONS
================================ */
[data-testid="stCheckbox"] label,
[data-testid="stRadio"] label {
    color: var(--text);
}

[data-testid="stCheckbox"] input:checked + div,
[data-testid="stRadio"] input:checked + div {
    background-color: var(--teal);
    border-color: var(--teal);
}

[data-testid="stCheckbox"] label:hover,
[data-testid="stRadio"] label:hover {
    color: var(--teal);
}

/* ================================
   PILL-STYLE TABS
================================ */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    gap: 10px;
    background: rgba(8, 15, 29, 0.72);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 999px;
    padding: 7px;
    width: fit-content;
    max-width: 100%;
    overflow-x: auto;
}

[data-testid="stTabs"] button[data-baseweb="tab"] {
    background: transparent;
    color: var(--muted);
    border: 1px solid transparent;
    border-radius: 999px;
    padding: 9px 22px;
    font-weight: 600;
    white-space: nowrap;
    transition: all 0.25s ease;
}

[data-testid="stTabs"] button[data-baseweb="tab"]:hover {
    color: var(--teal);
    background: rgba(0, 212, 170, 0.07);
}

[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
    color: #031018 !important;
    background: linear-gradient(110deg, var(--teal), var(--sky)) !important;
    border-color: transparent !important;
    box-shadow: 0 0 20px rgba(0, 212, 170, 0.22);
}

[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    display: none;
}

/* ================================
   BUTTONS
================================ */
.stButton > button,
.stDownloadButton > button,
[data-testid="stFormSubmitButton"] button,
button[kind="primary"] {
    color: #031018 !important;
    background: linear-gradient(110deg, var(--teal), var(--sky)) !important;
    border: 1px solid transparent !important;
    border-radius: 999px !important;
    padding: 0.65rem 1.5rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.01em;
    box-shadow: 0 4px 18px rgba(0, 212, 170, 0.14);
    transition: transform 0.25s ease, box-shadow 0.25s ease, filter 0.25s ease;
}

.stButton > button:hover,
.stDownloadButton > button:hover,
[data-testid="stFormSubmitButton"] button:hover,
button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(0, 212, 170, 0.3);
    filter: brightness(1.06);
}

.stButton > button:active,
.stDownloadButton > button:active {
    transform: translateY(0) scale(0.98);
}

/* Secondary buttons */
button[kind="secondary"] {
    color: var(--teal) !important;
    background: rgba(0, 212, 170, 0.06) !important;
    border: 1px solid rgba(0, 212, 170, 0.3) !important;
    border-radius: 999px !important;
}

button[kind="secondary"]:hover {
    background: rgba(0, 212, 170, 0.13) !important;
    border-color: var(--teal) !important;
}

/* ================================
   DATAFRAMES & TABLES
================================ */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    border: 1px solid rgba(148, 163, 184, 0.15);
    border-radius: 14px;
    overflow: hidden;
    background: rgba(8, 15, 29, 0.75);
}

[data-testid="stDataFrame"] * {
    scrollbar-color: var(--teal) #0b1220;
}

[data-testid="stDataFrame"] [role="columnheader"] {
    background: #0d1928 !important;
    color: var(--teal) !important;
    font-weight: 700 !important;
}

/* ================================
   CHART CONTAINERS
================================ */
[data-testid="stPlotlyChart"],
[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"],
[data-testid="stAltairChart"],
[data-testid="stPyplotChart"] {
    background: rgba(11, 18, 32, 0.65);
    border: 1px solid rgba(148, 163, 184, 0.1);
    border-radius: 16px;
    padding: 10px;
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

[data-testid="stPlotlyChart"]:hover,
[data-testid="stVegaLiteChart"]:hover,
[data-testid="stAltairChart"]:hover {
    border-color: rgba(0, 212, 170, 0.25);
    box-shadow: 0 0 20px rgba(0, 212, 170, 0.04);
}

/* ================================
   ALERTS & STATUS MESSAGES
================================ */
[data-testid="stAlert"] {
    background: rgba(11, 18, 32, 0.88);
    border: 1px solid rgba(56, 189, 248, 0.22);
    border-radius: 14px;
    backdrop-filter: blur(12px);
}

[data-testid="stNotificationContentSuccess"] {
    color: var(--teal);
}

[data-testid="stAlert"][kind="success"] {
    border-color: rgba(0, 212, 170, 0.3);
}

[data-testid="stAlert"][kind="error"] {
    border-color: rgba(251, 113, 133, 0.35);
}

/* ================================
   PROGRESS BAR
================================ */
[data-testid="stProgressBar"] > div {
    background: rgba(148, 163, 184, 0.12);
    border-radius: 999px;
    overflow: hidden;
}

[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, var(--teal), var(--sky));
    box-shadow: 0 0 12px rgba(0, 212, 170, 0.35);
    border-radius: 999px;
}

/* ================================
   FILE UPLOADER
================================ */
[data-testid="stFileUploader"] section {
    background: rgba(8, 15, 29, 0.72);
    border: 1px dashed rgba(0, 212, 170, 0.3);
    border-radius: 16px;
    transition: border-color 0.25s ease, background 0.25s ease;
}

[data-testid="stFileUploader"] section:hover {
    border-color: var(--teal);
    background: rgba(0, 212, 170, 0.04);
}

[data-testid="stFileUploader"] button {
    border-radius: 999px !important;
}

/* ================================
   EXPANDERS
================================ */
[data-testid="stExpander"] {
    background: rgba(11, 18, 32, 0.65);
    border: 1px solid rgba(148, 163, 184, 0.13);
    border-radius: 14px;
    overflow: hidden;
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

[data-testid="stExpander"]:hover {
    border-color: rgba(0, 212, 170, 0.3);
    box-shadow: 0 0 16px rgba(0, 212, 170, 0.05);
}

[data-testid="stExpander"] summary {
    padding: 12px 16px;
    font-weight: 600;
}

[data-testid="stExpander"] summary:hover {
    color: var(--teal);
}

/* ================================
   DIVIDERS
================================ */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(0, 212, 170, 0.3),
        rgba(56, 189, 248, 0.2),
        transparent
    );
    margin: 1.5rem 0;
}

/* ================================
   CUSTOM TEAL SCROLLBAR
================================ */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #030712;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--teal), #087f8c);
    border-radius: 10px;
    border: 2px solid #030712;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, var(--sky), var(--teal));
}

* {
    scrollbar-width: thin;
    scrollbar-color: var(--teal) #030712;
}

/* ================================
   LINKS & SELECTION
================================ */
a {
    color: var(--sky);
    text-decoration: none;
    transition: color 0.2s ease;
}

a:hover {
    color: var(--teal);
}

::selection {
    color: #030712;
    background: var(--teal);
}

/* ================================
   SPINNER
================================ */
[data-testid="stSpinner"] > div {
    border-top-color: var(--teal) !important;
}

/* ================================
   STATUS WIDGET
================================ */
[data-testid="stStatusWidget"] {
    background: rgba(11, 18, 32, 0.9);
    border: 1px solid var(--border);
    border-radius: 12px;
}

/* ================================
   FOOTER
================================ */
footer {
    visibility: hidden;
}

[data-testid="stFooter"] {
    background: transparent;
}

/* ================================
   RESPONSIVE DESIGN
================================ */
@media (max-width: 768px) {
    .block-container {
        padding: 1.25rem 1rem 2rem;
    }

    h1 {
        font-size: 2rem !important;
    }

    [data-testid="stMetric"] {
        padding: 16px;
        border-radius: 14px;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.5rem !important;
    }

    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        width: 100%;
        border-radius: 16px;
    }

    [data-testid="stTabs"] button[data-baseweb="tab"] {
        padding: 8px 14px;
    }
}

/* ================================
   ACCESSIBILITY
================================ */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
</style>
""", unsafe_allow_html=True)

PALETTE = ['#00d4aa', '#38dbf8', '#fbbf24', '#a78bfa', '#b923cc']

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&display=swap');

.dashboard-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.3rem;
    font-weight: 800;
    background: linear-gradient(90deg, #00d4aa, #38bdf8, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.35rem;
    line-height: 1.3;
}

.dashboard-subtitle {
    font-size: 0.95rem;
    color: rgba(255, 255, 255, 0.40);
    margin-top: 0;
    margin-bottom: 1.8rem;
    font-family: sans-serif;
}
</style>

<h1 class="dashboard-title">Healthcare Intelligence Dashboard</h1>
<p class="dashboard-subtitle">Real-time patient &amp; financial analytics</p>
""", unsafe_allow_html=True)



CHART_THEME = dict(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',

    font=dict(
        color='#e5edf7',
        size=12,
        family='DM Sans'
    ),

    xaxis=dict(
        gridcolor='rgba(255,255,255,0.06)',
        showline=False,
        zeroline=False
    ),

    yaxis=dict(
        gridcolor='rgba(255,255,255,0.06)',
        showline=False,
        zeroline=False
    ),

    margin=dict(l=10, r=10, t=40, b=10),

    colorway=PALETTE
)

# st.button(label=" Refresh Data",on_click=st.cache_data.clear)
# load_data
@st.cache_data
# To this:
@st.cache_data
def load_data():
    df = pd.read_excel('Healthcare report.xlsx')
    return df
df = load_data()

# print(df.to_string())
print(df.head())

base_df = df.copy()

base_df['Date of Admission'] = pd.to_datetime(base_df['Date of Admission'], format = '%d-%m-%Y')

base_df['Discharge Date'] = pd.to_datetime(base_df['Discharge Date'], format = '%d-%m-%Y')

base_df['Stay Days'] = (base_df['Discharge Date'] - base_df['Date of Admission']).dt.days

base_df['Age Group'] = pd.cut(
    base_df['Age'],
    bins = [0, 18, 30, 40, 50, 120],
    labels = ['Kids','Adult','Mid','Senior', 'Old']

)

base_df['Name']  = base_df['Name'].str.title()

st.sidebar.title('🏥  Filters')

with st.sidebar.expander('Basic Filter', expanded= True):
    min_date = base_df['Date of Admission'].min().date()
    max_date = base_df['Date of Admission'].max().date()

    date_range = st.date_input('Date Range', value = (min_date,max_date), min_value= min_date, max_value= max_date)

    if isinstance(date_range, (list,tuple)) and len(date_range) == 2:
        start_date, end_date = date_range

    else:
          start_date, end_date = min_date, max_date

    medical_condition = st.multiselect('Medical Condition',
                                       options= sorted(base_df['Medical Condition'].unique()),
                                       default= sorted(base_df['Medical Condition'].unique()))


    admission_type = st.multiselect('Admission Type',
                                    options = sorted(base_df['Admission Type'].unique()),
                                    default = sorted(base_df['Admission Type'].unique()))


    with st.sidebar.expander('Advanced Filters'):

     insurance_provider = st.multiselect(
        'Insurance Provider',
        options = sorted(base_df['Insurance Provider'].unique()),
        default = sorted(base_df['Insurance Provider'].unique())
                         )


    gender = st.multiselect(
        'Gender',
        options=sorted(base_df['Gender'].unique()),
        default=sorted(base_df['Gender'].unique())
    )

    age_group = st.multiselect(
        'Age Group',
        options=['Kids', 'Adult', 'Mid', 'Senior', 'Old'],
        default= ['Kids', 'Adult', 'Mid', 'Senior', 'Old']
    )


df = base_df[
    (base_df['Date of Admission'] >= pd.to_datetime(start_date)) &
    (base_df['Date of Admission'] <= pd.to_datetime(end_date)) &
    (base_df['Medical Condition'].isin(medical_condition)) &
    (base_df['Admission Type'].isin(admission_type))  &
    (base_df['Insurance Provider'].isin(insurance_provider))  &
    (base_df['Gender'].isin(gender))  &
    (base_df['Age Group'].isin(age_group))

]

total_days = (end_date - start_date).days + 1

prev_start = start_date - timedelta(days = total_days)

prev_end = start_date - timedelta(days= 1)



prev_df = base_df[
    (base_df['Date of Admission'] >= pd.to_datetime(prev_start)) &
    (base_df['Date of Admission'] <= pd.to_datetime(prev_end)) &
    (base_df['Medical Condition'].isin(medical_condition)) &
    (base_df['Admission Type'].isin(admission_type))  &
    (base_df['Insurance Provider'].isin(insurance_provider))  &
    (base_df['Gender'].isin(gender))  &
    (base_df['Age Group'].isin(age_group))

]

def get_delta(current, previous):

    if previous == 0 or pd.isna(previous) or pd.isna(current):
        return 'N/A (no prev data)'

    change = ((current - previous) / previous) * 100

    return f'{change:.1f}% vs prev'


cur_bill = df['Billing Amount'].sum()

prev_bill = prev_df['Billing Amount'].sum()

cur_adm = len(df)

prev_adm = len(prev_df)


cur_avg = df['Billing Amount'].mean()  if len(df)  else 0

prev_avg = prev_df['Billing Amount'].mean() if len(prev_df)  else 0


cur_stay = df['Stay Days'].mean()  if len(df) else 0

prev_stay = prev_df['Stay Days'].mean()  if len(df)  else 0


st.caption(f'Previous:  {prev_start}  ->  {prev_end}   | Current: {start_date}   -> {end_date} ')


col1, col2, col3, col4  = st.columns(4)

col1.metric('Total Billing', f'₹{cur_bill:,.0f}', get_delta(cur_bill,prev_bill))

col2.metric('Total Admission',f'{cur_adm:,}',get_delta(cur_adm,prev_adm))

col3.metric('AVG Billing / Admission', f'₹{cur_avg:,.0f}', get_delta(cur_avg,prev_avg))

col4.metric('AVG Stay Days', f'{cur_stay:,.1f}', get_delta(cur_stay,prev_stay))


st.divider()


tab1, tab2, tab3 = st.tabs(['Patient Intelligence', '💰 Financial Intelligence', ' 🗎 Raw Data'])



with tab1:
    col1, col2, col3, col4 = st.columns(4)

    col1.metric('Unique Patient (by name)', f'{df['Name'].nunique():}')
    col2.metric('Average Age', f'{df['Age'].mean():.0f} yrs ')
    col3.metric('Avg Stay', f'{df['Stay Days'].mean():.1f} days')
    col4.metric('Emergency Rate', f'{(df['Admission Type'] == 'Emergency').mean() *100:.1f}%')

    st.divider()


    st.subheader('Demographics')


    col1, col2, col3 = st.columns(3)


    with col1:
        age_data = df['Age Group'].value_counts().reset_index()
        age_data.columns = ['Age Group', 'Count']


        fig = px.bar(age_data, x = 'Age Group', y = 'Count', text = 'Count',
                     title = 'Age Group Distribution',
                     color = 'Age Group', color_discrete_sequence= PALETTE)


        fig.update_traces(textposition = 'outside', marker_line_width = 0)

        fig.update_layout(**CHART_THEME, showlegend = False)

        st.plotly_chart(fig, use_container_width= True)



    with col2:

        gender_data = df['Gender'].value_counts().reset_index()
        gender_data.columns = ['Gender', 'Count']

        fig = px.pie(gender_data, names= 'Gender', values= 'Count',
                     title = 'Gender Distribution',
                     color_discrete_sequence= PALETTE, hole= 0.5)

        fig.update_layout(**CHART_THEME)

        st.plotly_chart(fig, use_container_width= True)



    with col3:
        cond_data =  df['Medical Condition'].value_counts().reset_index()
        cond_data.columns = ['Condition', 'Count']

        fig = px.bar(cond_data, x = 'Condition', y = 'Count',
                     title = 'Medical Condition',
                     color = 'Condition',
                     color_discrete_sequence = PALETTE )

        fig.update_traces(textposition = 'outside', marker_line_width = 0)

        fig.update_layout(**CHART_THEME, showlegend = False, xaxis_tickangle = -30)

        st.plotly_chart(fig, use_container_width= True)


    blood_data = df['Blood Type'].value_counts().sort_values().reset_index()

    blood_data.columns = ['Blood Type', 'Count']

    blood_data['Pct'] = (blood_data['Count'] / blood_data['Count'].sum() * 100).round(1)

    fig = px.bar(
        blood_data,
        x = 'Count', y = 'Blood Type',
        orientation= 'h',
        text = blood_data['Pct'].astype(str) + '%',
        title = 'Blood Type Distribution',
        color = 'Blood Type', color_discrete_sequence= PALETTE

    )

    fig.update_traces(textposition = 'outside', marker_line_width =0)
    fig.update_layout(**CHART_THEME, showlegend = False)
    st.plotly_chart(fig, use_container_width= True)


with tab2:
    col1, col2, col3, col4 = st.columns(4)

    col1.metric('Total Revenue', f'{df['Billing Amount'].sum():,.0f}')
    col2.metric('Avg Billing', f'{df['Billing Amount'].mean():,.0f}')
    col3.metric('Max Bill', f'{df['Billing Amount'].max():,.0f}')
    col4.metric('Min Bill', f'{df['Billing Amount'].min():,.0f}')

    st.divider()

    col1, col2 = st.columns(2)


    with col1:

        cond_rev = df.groupby('Medical Condition')['Billing Amount'].sum().reset_index()
        cond_rev.columns = ['Condition', 'Revenue']

        cond_rev = cond_rev.sort_values('Revenue', ascending= True)

        fig = px.bar(
            cond_rev,
            x = 'Revenue' , y = 'Condition',
            orientation= 'h',
            title = 'Revenue by Medical Condition',
            color = 'Condition', color_discrete_sequence= PALETTE,
            text = 'Revenue'

        )

        fig.update_traces(texttemplate =  '₹%{text:,.0f},', textposition = 'outside', marker_line_width = 0)

        fig.update_layout(**CHART_THEME)

        st.plotly_chart(fig,use_container_width= True)

    with col2:

        ins_rev = df.groupby('Insurance Provider')['Billing Amount'].sum().reset_index()

        ins_rev.columns = ['Provider', 'Revenue']

        fig = px.pie(
            ins_rev,
            names = 'Provider',
            values= 'Revenue',
            title = 'Revenue by Insurance Provider',
            color_discrete_sequence= PALETTE, hole =0.45

        )

        fig.update_layout(**CHART_THEME)

        st.plotly_chart(fig, use_container_width= True)


with tab3:

    st.markdown(f'{len(df):,} Records')

    st.dataframe(
        df.sort_values('Date of Admission', ascending= False),
        use_container_width= True,
        height = 500
    )



