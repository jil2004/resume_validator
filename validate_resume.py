import sys
import re
from pdfminer.high_level import extract_text

def validate_resume():
    if len(sys.argv) != 2:
        print("Usage: python validate_resume.py <filename>")
        return False

    filename = sys.argv[1]

    # Extract the text from the PDF file
    with open(filename, 'rb') as file:
        resume_text = extract_text(file)

    print(resume_text) # print the extracted text

    # Check for certain keywords or phrases in the resume text
    required_skills = ['Python', 'Java', 'JavaScript', 'SQL']
    required_experience = ['years of experience', 'months of experience']
    for skill in required_skills:
        if not re.search(skill, resume_text, re.IGNORECASE):
            print(f"Skill '{skill}' not found.")
            return False
    for exp in required_experience:
        if not re.search(exp, resume_text, re.IGNORECASE):
            print(f"Experience '{exp}' not found.")
            return False

    print("Resume is valid.")
    return True

if __name__ == "__main__":
    validate_resume()
