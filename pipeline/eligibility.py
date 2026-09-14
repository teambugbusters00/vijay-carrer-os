import re
from .models import Job

POSITIVE = [r"india", r"worldwide", r"everywhere", r"global", r"anywhere"]
NEGATIVE = [r"us only", r"usa only", r"united states only", r"canada only", r"must be based in", r"must reside in"]

def classify(job: Job, profile: dict) -> Job:
    text = " ".join([job.location, job.description, job.work_authorization]).lower()
    if any(re.search(pattern, text) for pattern in NEGATIVE) and "india" not in text:
        job.eligibility = "no"
        job.eligibility_reason = "Listing appears geographically restricted."
        return job
    if any(re.search(pattern, text) for pattern in POSITIVE):
        job.eligibility = "yes"
        job.eligibility_reason = "India/worldwide eligibility signal found."
    elif job.remote_status == "remote":
        job.eligibility = "unknown"
        job.eligibility_reason = "Remote is stated, but India eligibility is not explicit."
    else:
        job.eligibility = "no"
        job.eligibility_reason = "Not identified as a suitable remote role."
    return job
