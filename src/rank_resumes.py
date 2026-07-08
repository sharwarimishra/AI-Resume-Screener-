import os
from sentence_transformers import SentenceTransformer, util

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def rank_resumes(resumes_folder, jd_path):
    """Ranks all resume .txt files in a folder against a job description."""
    model = SentenceTransformer('all-MiniLM-L6-v2')

    jd_text = read_text_file(jd_path)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    results = []

    for filename in os.listdir(resumes_folder):
        if filename.endswith(".txt"):
            resume_path = os.path.join(resumes_folder, filename)
            resume_text = read_text_file(resume_path)

            resume_embedding = model.encode(resume_text, convert_to_tensor=True)
            score = util.cos_sim(resume_embedding, jd_embedding)
            score = float(score[0][0]) * 100

            results.append((filename, score))

    # Sort by score, highest first
    results.sort(key=lambda x: x[1], reverse=True)

    return results


if __name__ == "__main__":
    ranked = rank_resumes("../output", "../data/job_description.txt")

    print("\n=== Resume Ranking ===")
    for rank, (filename, score) in enumerate(ranked, start=1):
        print(f"{rank}. {filename} — {score:.2f}%")