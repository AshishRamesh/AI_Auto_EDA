import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components

# Streamlit page settings
st.set_page_config(page_title="Auto EDA - Dark Mode Profiling", layout="wide")

# Page title
st.title("Auto EDA - Data Profiling in Dark Mode 🌙")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

    # Generate YData profile report
    profile = ProfileReport(df, title="Auto EDA - Dark Mode Report", explorative=True)

    # Convert report to HTML
    report_html = profile.to_html()

    # Inject dark theme CSS
    dark_css = """
    <style>
    body { background-color: #0E1117 !important; color: #FFFFFF !important; }
    .container { background-color: #0E1117 !important; color: #FFFFFF !important; }
    .alert-info, .alert-warning, .alert-danger { background-color: #333 !important; color: #FFFFFF !important; }
    table { background-color: #1E1E1E !important; color: #FFFFFF !important; }
    th, td { border-color: #555 !important; }
    h1, h2, h3, h4, h5, h6 { color: #39FF14 !important; }
    </style>
    """

    # Combine dark mode CSS with report HTML
    report_html = dark_css + report_html

    # Render report inside Streamlit
    components.html(report_html, height=1000, scrolling=True)

else:
    st.warning("⚠ Please upload a file to generate the report.")
