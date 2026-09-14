from .models import Job

def normalize(raw: dict, source: str) -> Job:
    return Job(
        source=source,
        title=raw.get("title", "").strip(),
        company=raw.get("company", "").strip(),
        url=raw.get("url", "").strip(),
        location=raw.get("location", "").strip(),
        remote_status=raw.get("remote_status", "unknown"),
        description=raw.get("description", ""),
        compensation=raw.get("compensation", ""),
        posted_at=raw.get("posted_at"),
        deadline=raw.get("deadline"),
        skills=raw.get("skills", []),
        experience=raw.get("experience", ""),
        work_authorization=raw.get("work_authorization", ""),
        raw=raw,
    )
