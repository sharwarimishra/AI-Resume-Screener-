import re

def extract_email(text):
    """Finds an email address in the text using regex."""
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    if match:
        return match.group()
    return None


def extract_phone(text):
    """Finds a phone number in the text using regex."""
    match = re.search(r'(\+?\d{1,3}[-\s]?)?\d{10}', text)
    if match:
        return match.group()
    return None


def extract_skills(text, skill_list):
    """Checks which skills from skill_list appear in the resume text."""
    text_lower = text.lower()
    found_skills = []
    for skill in skill_list:
        if skill.lower() in text_lower:
            found_skills.append(skill)
    return found_skills


if __name__ == "__main__":
    with open("../output/sample_resume.txt", "r", encoding="utf-8") as f:
        resume_text = f.read()

    email = extract_email(resume_text)
    phone = extract_phone(resume_text)

    skill_list = ["Python", "Java", "SQL", "XGBoost", "LSTM", "GRU",
                  "Machine Learning", "MATLAB", "Simulink", "Deep Learning"]
    skills_found = extract_skills(resume_text, skill_list)

    print("Email:", email)
    print("Phone:", phone)
    print("Skills found:", skills_found)