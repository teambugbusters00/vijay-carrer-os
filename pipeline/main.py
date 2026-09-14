from pathlib import Path
import yaml
from .deduplicator import deduplicate
from .eligibility import classify
from .matcher import match

ROOT = Path(__file__).resolve().parents[1]

def load_profile():
    return yaml.safe_load((ROOT / "config/profile.yaml").read_text())

def run(jobs=None):
    profile = load_profile()["profile"]
    jobs = deduplicate(jobs or [])
    for job in jobs:
        classify(job, profile)
        match(job, profile)
    return sorted(jobs, key=lambda item: item.fit_score, reverse=True)

if __name__ == "__main__":
    print("Pipeline scaffold ready. Add compliant source adapters under scrapers/.")
