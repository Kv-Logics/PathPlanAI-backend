from typing import List, Dict

# Simple skill keywords for prototype
KNOWN_SKILLS = [
    "python", "java", "c++", "sql", "javascript",
    "fastapi", "flask", "react", "node",
    "machine learning", "deep learning",
    "data analysis", "git", "docker"
]

def extract_skills(resume_text: str) -> List[str]:
    resume_text = resume_text.lower()
    found_skills = []

    for skill in KNOWN_SKILLS:
        if skill in resume_text:
            found_skills.append(skill)

    return list(set(found_skills))


def build_capability_map(resume_text: str) -> Dict:
    skills = extract_skills(resume_text)

    capability_map = {
        "total_skills_detected": len(skills),
        "skills": skills,
        "readiness_score": min(len(skills) * 10, 100)  # simple heuristic
    }

    return capability_map
