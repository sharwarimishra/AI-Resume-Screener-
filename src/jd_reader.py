def read_job_description(jd_path):
    """Reads a job description text file and returns its content."""
    with open(jd_path, "r", encoding="utf-8") as f:
        jd_text = f.read()
    return jd_text


if __name__ == "__main__":
    jd_text = read_job_description("../data/job_description.txt")
    print("Job Description Loaded:")
    print(jd_text)