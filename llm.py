import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configure Gemini Pro
API_KEY = "AIzaSyAii2MFjkODf7DJMOMbtxggimos4-z1A3c"
genai.configure(api_key=API_KEY)

# Set page configuration
st.set_page_config(page_title="LLM Chatbot", layout="wide")

# Custom CSS for better readability
st.markdown("""
<style>
    body {
        color: #333;
        background-color: #f0f2f6;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #1e3a8a;
    }
    .stButton > button {
        background-color: #1e3a8a;
        color: white;
        font-weight: bold;
    }
    .stTextInput > div > div > input {
        color: #333;
    }
    .stSelectbox > div > div > select {
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

def generate_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("LLM CHATBOT")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Load and display the dataset
        df = pd.read_csv(uploaded_file)

        # Display dataset preview
        st.header("Dataset Preview")
        st.dataframe(df.head())

        # Show dataset summary
        st.header("Summary of Dataset")
        summary_prompt = f"Summarize the following dataset:\n\n{df.describe().to_string()}\n\nProvide key insights and trends."
        summary = generate_response(summary_prompt)
        st.write(summary)

        # Handle user queries
        st.header("Free to Ask Your Questions")
        user_input = st.text_input("Enter your question:")

        if user_input:
            question_prompt = f"Based on the following dataset:\n\n{df.head().to_string()}\n\nAnswer the following question: {user_input}"
            answer = generate_response(question_prompt)
            st.subheader("Answer")
            st.write(answer)

# Corrected entry point
if __name__ == "__main__":
    main()
