
import streamlit as st
from gemini import analyze_resume
from pdf_reader import extract_text_from_pdf

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")

st.write("Welcome to the AI Resume Analyzer!")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":

        resume_text = extract_text_from_pdf(uploaded_file)
        analysis = analyze_resume(resume_text)

        st.subheader("🤖 AI Resume Analysis")
        st.write(analysis)

        st.success("Resume uploaded successfully!")

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )