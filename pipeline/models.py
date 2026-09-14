from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Job:
    source: str
    title: str
    company: str
    url: str
    location: str = ""
    remote_status: str = "unknown"
    description: str = ""
    compensation: str = ""
    posted_at: Optional[str] = None
    deadline: Optional[str] = None
    skills: List[str] = field(default_factory=list)
    experience: str = ""
    work_authorization: str = ""
    raw: dict = field(default_factory=dict)
    eligibility: str = "unknown"
    eligibility_reason: str = ""
    fit_score: float = 0.0
