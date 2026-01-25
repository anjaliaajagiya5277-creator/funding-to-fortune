import streamlit as st
import pandas as pd
import pickle as pk
dt_model=pk.load(open('model.pkl','rb'))
scaler=pk.load(open('scaler.pkl','rb'))
st.set_page_config(
    page_title="From Funding to Fortune",
    page_icon="🚀",
    layout="wide"
)
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f7f7e8, #ffffff);
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* 🔥 GLOBAL TEXT COLOR OVERRIDE */
html, body, p, span, div, label, li {
    color: white !important;   /* change color here */
}

/* Slider labels & values */
.stSlider * {
    color: black !important;
}

/* Selectbox selected text */
div[data-baseweb="select"] > div {
    color: white !important;
}

/* Dropdown options */
ul[role="listbox"] li {
    color: black !important;
}

/* Radio button text */
div[role="radiogroup"] label {
    color: black !important;
}

/* Headings (if still white) */
h1, h2, h3, h4, h5, h6 {
    color: black !important;
}

/* Markdown containers */
[data-testid="stMarkdownContainer"] * {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0b0b0b;
}
section[data-testid="stSidebar"] {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<h1 style="color:maroon; font-size:34px;">
🚀 From Funding to Fortune
</h1>
<p style="color:#b0b0b0; margin-top:-10px;">
Predicting Startup Profitability using AI & ML
</p>
<hr style="border:1px solid #333;">
""", unsafe_allow_html=True)
left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown("""
    <h3 style="
    color:maroon;
    font-weight:700;
    display:flex;
    align-items:center;
    gap:8px;
    ">
    🏢 Business Attributes
    </h3>
    """, unsafe_allow_html=True)

    ind_type = st.selectbox(
        "Industry Type",
        ['IoT','EdTech','Gaming','AI','HealthTech','FinTech','Cybersecurity','E-Commerce']
    )

    Region = st.selectbox(
        "Region",
        ['Europe', 'South America', 'Australia', 'North America', 'Asia']
    )

    Exit_Status = st.radio(
        "Exit Status",
        ["Private", "Acquired", "IPO"],
        horizontal=True
    )

    year_founded = st.slider("Year Founded", 1990, 2025)
    Employees = st.slider("Number of Employees", 0, 5000)

with right_col:
    st.markdown("""
    <h3 style="
    color:maroon;
    font-weight:700;
    display:flex;
    align-items:center;
    gap:8px;
    ">
    💰 Financial Attributes
    </h3>
    """, unsafe_allow_html=True)

    no_of_funding_round = st.slider("Funding Rounds", 0, 5)
    Funding_Amount = st.slider("Funding Amount (M USD)", 0.0, 300.0)
    Valuation = st.slider("Valuation (M USD)", 0.0, 5000.0)
    Revenue = st.slider("Revenue (M USD)", 0.0, 100.0)
    Market_Share = st.slider("Market Share (%)", 0.0, 10.0)
st.markdown("<br>", unsafe_allow_html=True)


if ind_type=='AI':
    ind_type=0
elif ind_type=='Cybersecurity':
    ind_type=1
elif ind_type=='E-Commerce':
    ind_type=2
elif ind_type=='EdTech':
    ind_type=3
elif ind_type=='FinTech':
    ind_type=4
elif ind_type=='Gaming':
    ind_type=5
elif ind_type=='HealthTech':
    ind_type=6
else :
    ind_type=7
if Region=='Asia':
    Region=0
elif Region=='Australia':
    Region=1
elif Region=='Europe':
    Region=2
elif Region=='North America':
    Region=3
else :
    Region=4
if Exit_Status=='Private':
    Exit_Status=2
elif Exit_Status=='Acquired':
    Exit_Status=0
else:
    Exit_Status=1

st.markdown("""
<style>
/* Hide default Streamlit button */
div.stButton > button {
    background: linear-gradient(135deg, #ff3c3c, #ff7a18);
    color: black;
    font-size: 20px;
    font-weight: 700;
    padding: 14px 45px;
    border-radius: 14px;
    border: none;
    box-shadow: 0 0 15px rgba(255,60,60,0.6);
    transition: all 0.3s ease-in-out;
}

/* Hover effect */
div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(255, 122, 24, 0.9);
    background: linear-gradient(135deg, #ff7a18, #ff3c3c);
}
</style>
""", unsafe_allow_html=True)

# predict = st.button("🚀 Predict Startup Outcome")

if st.button("🚀 Predict Startup Outcome", key="predict_button_main"):

    pred_data =pd.DataFrame([[ind_type,no_of_funding_round,Funding_Amount,Valuation,Revenue,Market_Share,year_founded,Region,Exit_Status,Employees]],columns=['Industry','Funding Rounds','Funding Amount (M USD)','Valuation (M USD)','Revenue (M USD)','Employees','Market Share (%)','Year Founded','Region','Exit Status'])
    pred_data = scaler.transform(pred_data)
    predict = dt_model.predict(pred_data)
    if predict == 1:
        st.markdown("""
        <div style="
            background-color:#e6ffe6;
            color:green;
            padding:20px;
            border-radius:12px;
            font-size:22px;
            font-weight:bold;
            text-align:center;">
            🚀 This startup is likely to be PROFITABLE
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background-color:#ffe6e6;
            color:red;
            padding:20px;
            border-radius:12px;
            font-size:22px;
            font-weight:bold;
            text-align:center;">
            📉 This startup is likely to be NOT PROFITABLE
        </div>
        """, unsafe_allow_html=True)