# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python, Streamlit, and Google Gemini API**. The application analyzes resumes, provides ATS scores, identifies missing skills, suggests improvements, and recommends suitable job roles.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 🤖 AI-powered ATS Resume Analysis
- 📊 ATS Score Generation
- ✅ Resume Strengths & Weaknesses
- 💡 Skill Gap Analysis
- 📝 Resume Improvement Suggestions
- 💼 Job Role Recommendations
- ⚡ Fast and Interactive Streamlit Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyPDF2
- python-docx
- python-dotenv

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│── app.py
│── analyzer.py
│── gemini.py
│── pdf_reader.py
│── prompts.py
│── requirements.txt
│── .gitignore
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/HemalathaSana20/AI-Resume-Analyzer.git
```

### Go to the project folder

```bash
cd AI-Resume-Analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file in the project folder.

```
GEMINI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your own Google AI Studio API key.

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 📸 Output

The application provides:

- ATS Score
- Resume Strengths
- Resume Weaknesses
- Missing Skills
- Improvement Suggestions
- Recommended Job Roles

---

## 📌 Future Enhancements

- DOCX Resume Support
- Resume Keyword Matching
- Cover Letter Generator
- Interview Question Generator
- Resume Ranking
- Multi-language Resume Analysis

---

## 👩‍💻 Author

**Sana Hemalatha**

GitHub: https://github.com/HemalathaSana20
