import streamlit as st
import os
import sys

sys.path.append("src")

from parser import extract_text_from_pdf
from skill_extractor import extract_email, extract_phone, extract_skills
from sentence_transformers import SentenceTransformer, util

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 AI Resume Screening System")
st.write("Upload resumes and a job description to get ranked matches.")

# --- Cache the model so it loads only once ---
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

# --- Skills list used for matching ---
SKILL_LIST = ["Python", "Java", "SQL", "XGBoost", "LSTM", "GRU",
              "Machine Learning", "MATLAB", "Simulink", "Deep Learning",
              "AWS", "Cloud", "Data Preprocessing", "Feature Engineering"]

st.header("1. Job Description")
jd_text = st.text_area("Paste the job description here:", height=200)

st.header("2. Upload Resumes")
uploaded_files = st.file_uploader(
    "Upload one or more resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Rank Resumes"):
    if not jd_text.strip():
        st.error("Please paste a job description first.")
    elif not uploaded_files:
        st.error("Please upload at least one resume.")
    else:
        with st.spinner("Analyzing resumes..."):
            model = load_model()  # instant after the first time
            jd_embedding = model.encode(jd_text, convert_to_tensor=True)

            results = []
            for uploaded_file in uploaded_files:
                temp_path = os.path.join("data", uploaded_file.name)
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                resume_text = extract_text_from_pdf(temp_path)
                resume_embedding = model.encode(resume_text, convert_to_tensor=True)

                score = util.cos_sim(resume_embedding, jd_embedding)
                score = float(score[0][0]) * 100

                email = extract_email(resume_text)
                phone = extract_phone(resume_text)
                skills_found = extract_skills(resume_text, SKILL_LIST)

                results.append({
                    "filename": uploaded_file.name,
                    "score": score,
                    "email": email,
                    "phone": phone,
                    "skills": skills_found
                })

            results.sort(key=lambda x: x["score"], reverse=True)

        st.header("3. Ranked Results")
        for rank, candidate in enumerate(results, start=1):
            st.subheader(f"{rank}. {candidate['filename']} — {candidate['score']:.2f}% match")
            st.progress(int(candidate['score']))

            col1, col2 = st.columns(2)
            with col1:
                st.write(f"📧 **Email:** {candidate['email'] or 'Not found'}")
            with col2:
                st.write(f"📞 **Phone:** {candidate['phone'] or 'Not found'}")

            if candidate['skills']:
                st.write("🛠️ **Matched Skills:** " + ", ".join(candidate['skills']))
            else:
                st.write("🛠️ **Matched Skills:** None found")

            st.divider()