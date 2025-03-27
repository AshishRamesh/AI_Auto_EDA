import streamlit as st

def Home():
    # st.set_page_config(page_title="Auto EDA", layout="wide")
    st.markdown("""
    <style>
    .header {
        text-align: center;
        color: #39FF14;
        font-size: 3rem;
        font-weight: bold;
        padding-top: 0px;
    }
    .subheader {
        text-align: center;
        color: #fff;
        font-size: 1.5rem;
        margin-top: 0px;
        padding-bottom: 10px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        padding-top: 20px;
    }
    .stImage {
        max-width: 100%;
        margin-top: 20px;
        border-radius: 8px;
    }
    .footer {
        text-align: center;
        font-size: 1rem;
        color: #39FF14;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="header-container">
        <h1 class="header">Welcome to Auto EDA 📊</h1>
        <p class="subheader">AI-powered Exploratory Data Analysis for seamless insights and visualization.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    **Auto EDA** is a powerful tool designed to help data analysts and scientists explore datasets effortlessly. 
    Gain meaningful insights, visualize trends, and automate your EDA workflow with ease.

    **Key Features:**
    - Automated data profiling for quick insights.
    - Interactive visualizations to understand trends and patterns.
    - Outlier detection, missing value analysis, and feature correlation.
    - Support for `.csv`, `.xlsx` data formats.
    - AI-driven recommendations for deeper data understanding.

    Whether you're a beginner or an expert, **Auto EDA** simplifies your data exploration process.
    """)
    st.markdown("""
    <div class="footer">
        Developed by [Your Name or Team]
    </div>
    """, unsafe_allow_html=True)
    # with st.sidebar:
   

    

pg = st.navigation([st.Page(Home), st.Page("Auto-EDA.py"), st.Page("AI-EDA.py")])
pg.run()


