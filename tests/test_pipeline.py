from pipeline.models import Job
from pipeline.eligibility import classify
from pipeline.matcher import match

def test_india_remote():
    profile = {"skills": {"x": ["Python", "React"]}, "roles": ["AI Engineer Intern"]}
    job = Job(source="test", title="AI Engineer Intern", company="Acme", url="https://example.com", location="Remote India", remote_status="remote", description="Python React")
    classify(job, profile)
    match(job, profile)
    assert job.eligibility == "yes"
    assert job.fit_score > 0
