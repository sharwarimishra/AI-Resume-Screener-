# 📄 AI Resume Screening System

An AI-powered tool that automatically screens and ranks resumes against a job description using Natural Language Processing (NLP) and semantic similarity search.

## 🚀 What It Does

Recruiters often manually sift through hundreds of resumes for a single job posting. This project automates that process by:

- Extracting text from resume PDFs
- Parsing key candidate details (email, phone number, skills)
- Comparing each resume's meaning (not just keywords) against a job description using a pre-trained sentence embedding model
- Ranking all candidates by relevance score
- Displaying results through an interactive web interface

## ✨ Features

- 📎 Bulk PDF resume upload
- 🧠 Semantic similarity matching using Sentence Transformers (goes beyond simple keyword matching)
- 🛠️ Automatic skill, email, and phone number extraction
- 📊 Ranked candidate list with visual match-score bars
- ⚡ Cached AI model for fast repeated use
- 🖥️ Clean, interactive UI built with Streamlit

## 🧰 Tech Stack

- **Python**
- **pdfplumber** — PDF text extraction
- **Sentence Transformers (all-MiniLM-L6-v2)** — semantic embeddings
- **Regex** — rule-based skill/contact extraction
- **Streamlit** — web interface

## ⚙️ How It Works

1. The user pastes a job description and uploads one or more resume PDFs.
2. Each resume is parsed and converted into plain text.
3. Both the resumes and job description are converted into numerical vector embeddings using a pre-trained transformer model.
4. Cosine similarity is calculated between each resume and the job description to produce a match score.
5. Skills, emails, and phone numbers are extracted using regex pattern matching.
6. Candidates are ranked and displayed with their match percentage and extracted details.

## 🖥️ Running It Locally

```bash
# Clone the repository
git clone https://github.com/sharwarimishra/AI-Resume-Screener-.git
cd AI-Resume-Screener-

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🔮 Future Improvements

- Support for `.docx` resumes
- Named Entity Recognition (NER) for smarter skill extraction
- Downloadable ranked report (CSV/PDF)
- Deployment on Streamlit Community Cloud for public live demo

## 👩‍💻 Author

**Sharwari Mishra**
B.Tech, Electrical & Computer Engineering
[GitHub](https://github.com/sharwarimishra) | [LinkedIn](#)