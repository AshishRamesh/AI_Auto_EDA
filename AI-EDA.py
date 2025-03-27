from openai import OpenAI
import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv('API_KEY'),  
)

st.title("Chat with AI-EDA 🤖")
st.subheader("Upload an Excel file and ask questions!")

with st.sidebar:
    st.info("🔍 **How it works:**\n1. Upload your file.\n2. Let the bot analyze it.\n3. Ask questions for insights.", icon="ℹ️")
    st.markdown("**Supported Formats:** `.xlsx`, `.csv`")
    st.markdown("---")
    st.text("🚀 Project by [Your Team Name]")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "data_summary" not in st.session_state:
    st.session_state["data_summary"] = None

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "csv"])

if uploaded_file:
    file_extension = uploaded_file.name.split('.')[-1]

    # Read the file
    if file_extension == "xlsx":
        df = pd.read_excel(uploaded_file, engine="openpyxl")  
    else:
        df = pd.read_csv(uploaded_file)

    st.success(f"Uploaded: {uploaded_file.name}")

    # Show metadata
    st.write("### File Summary:")
    # st.write(f"**Columns:** {list(df.columns)}")
    # st.write(f"**Total Rows:** {df.shape[0]}")

    # Let user select a column
    selected_column = st.selectbox("Select a column for analysis:", df.columns)

    # Limit rows to prevent exceeding token limit
    # row_limit = st.slider("Select number of rows to analyze:", min_value=5, max_value=min(100, len(df)), value=10)
    row_limit = 50
    # Show a preview
    st.write(f"**Preview of {selected_column} (first {row_limit} rows):**")
    st.write(df[selected_column].head(row_limit))

    # Generate summary for large datasets
    if df[selected_column].dtype in ['int64', 'float64']:  # Numerical column
        summary = df[selected_column].describe().to_dict()
    else:  # Categorical/text column
        summary = df[selected_column].value_counts().to_dict()

    st.write("### Column Summary:")
    st.write(summary)
    st.session_state["data_summary"] = summary

    # Allow user to enter a prompt
    if st.session_state["data_summary"]:
        # Display chat history
        for chat in st.session_state["chat_history"]:
            with st.chat_message(chat["role"]):
                st.write(chat["message"])

        # Input for user prompt
        if prompt := st.chat_input("Ask a question about the file..."):
            # Append user message to chat history
            st.session_state["chat_history"].append({"role": "user", "message": prompt})
            with st.chat_message("user"):
                st.write(prompt)

            # Generate AI response
            with st.spinner("Analyzing data..."):
                try:
                    response = client.chat.completions.create(
                        messages=[
                            {"role": "system", "content": "You are an AI data analyst. Use the summary of the file to answer queries."},
                            {"role": "user", "content": f"Dataset Summary:\n{st.session_state['data_summary']}\n\nUser Query: {prompt}"}
                        ],
                        model="gpt-4o",
                        max_tokens=500,  
                        n=1,  
                    )

                    response_text = response.choices[0].message.content  # Extract response

                    # Store AI response in chat history
                    st.session_state["chat_history"].append({"role": "ai", "message": response_text})

                    # Display AI response
                    with st.chat_message("ai"):
                        st.write(response_text)

                except Exception as e:
                    error_message = f"An error occurred: {e}"
                    st.session_state["chat_history"].append({"role": "ai", "message": error_message})
                    with st.chat_message("ai"):
                        st.write(error_message)

    # Footer
st.markdown("---")