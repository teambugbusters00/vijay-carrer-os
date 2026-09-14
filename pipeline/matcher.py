from rapidfuzz.fuzz import token_set_ratio
from .models import Job

def match(job: Job, profile: dict) -> Job:
    skill_values = []
    for group in profile.get("skills", {}).values():
        skill_values.extend(group)
    job_text = " ".join([job.title, job.description, " ".join(job.skills)]).lower()
    hits = sum(1 for skill in skill_values if str(skill).lower() in job_text)
    skill_score = min(100, hits / max(1, len(skill_values)) * 100 * 4)
    title_score = token_set_ratio(job.title.lower(), " ".join(profile.get("roles", [])).lower())
    eligibility_score = 100 if job.eligibility == "yes" else 45 if job.eligibility == "unknown" else 0
    job.fit_score = round(0.50 * skill_score + 0.25 * title_score + 0.25 * eligibility_score, 1)
    return job
