from .models import Job

def deduplicate(jobs: list[Job]) -> list[Job]:
    seen = set()
    out = []
    for job in jobs:
        key = (job.company.lower().strip(), job.title.lower().strip(), job.url.split("?")[0].rstrip("/"))
        if key not in seen:
            seen.add(key)
            out.append(job)
    return out
