def build_application_record(job, generated_text=""):
    return {
        "job_url": job.url,
        "company": job.company,
        "role": job.title,
        "fit_score": job.fit_score,
        "eligibility": job.eligibility,
        "generated_text": generated_text,
        "status": "needs_approval",
    }
