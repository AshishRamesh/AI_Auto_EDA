import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components

def home():
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
        <h1 class="header"> Auto EDA </h1>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.info("🔍 **How it works:**\n1. Upload your file.\n2. Let the bot analyze.\n3. Select View to obtain EDA. You can Download the file by selecting Download.", icon="ℹ️")
    st.markdown("**Supported Formats:** `.txt`, `.csv`")
    st.markdown("---")
    st.text("🚀 Project by ")
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    col1, col2, col3, col4= st.columns([1, 1, 1, 1])
    file_extension = uploaded_file.name.split('.')[-1]

    with st.expander("File Preview", expanded=True):
        # Read and Display File Content
        if file_extension in ["xlsx", "xls"]:
            data = pd.read_excel(uploaded_file, engine="openpyxl" if file_extension == "xlsx" else "xlrd")
            st.write("File Preview:")
            st.dataframe(data.head())
            # Convert Excel data to string format for LLM
            st.session_state["content"] = data.to_string(index=False)

    st.markdown("---")
    col1, col2, col3, col4= st.columns([1, 1, 1, 1])

    with col2:
        view_clicked = st.button("View", use_container_width=True, type = 'primary')
    with col3:
        download_clicked = st.button("Download", use_container_width=True)

    if download_clicked:
        pass
        # components.html(report_html, height=1000, scrolling=True)

    if view_clicked:
        with st.spinner("Generating..."):
            profile = ProfileReport(df, title="Auto EDA Report", explorative=True)
            report_html = profile.to_html()
            components.html(report_html, height=1000, scrolling=True)

else:
    st.warning("⚠ Please upload a file to generate the report.")
