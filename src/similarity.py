from sentence_transformers import SentenceTransformer, util

def calculate_similarity(resume_text, jd_text):
    """Calculates how semantically similar a resume is to a job description."""
    model = SentenceTransformer('all-MiniLM-L6-v2')

    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    similarity_score = util.cos_sim(resume_embedding, jd_embedding)

    return float(similarity_score[0][0])


if __name__ == "__main__":
    with open("../output/sample_resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()

    with open("../data/job_description.txt", "r", encoding="utf-8") as f:
        jd_text = f.read()

    score = calculate_similarity(resume_text, jd_text)
    print(f"Match Score: {score * 100:.2f}%") 