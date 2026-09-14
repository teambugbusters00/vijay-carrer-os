# Remote Job Agent

Automated discovery, eligibility filtering, CV matching, ranking, and approval-first application preparation for remote internships and entry-level roles.

## Safety model
- Discovery and ranking are automated.
- Application text is generated only from verified profile data.
- Submission is approval-first by default.
- No CAPTCHA bypassing, anti-bot bypassing, or fabricated application answers.
- Prefer canonical employer ATS/application pages.

## Pipeline
GitHub Actions -> collectors -> normalizer -> deduplicator -> India eligibility -> CV matcher -> ranker -> DB -> notifications -> approval queue.

## Sources
YC Work at a Startup, Himalayas, Wellfound, Startup Jobs, StartupHub.ai, Remote OK, We Work Remotely, Remotive, Working Nomads, Jobgether, Ashby, Greenhouse, Lever, and compliant company career pages.

## Setup
1. Configure `config/profile.yaml`.
2. Add GitHub Actions secrets from `.env.example`.
3. Set up PostgreSQL/Supabase using `database/schema.sql`.
4. Run `python -m pipeline.main` locally.

Portal adapters must respect each site's terms, robots rules, rate limits, authentication requirements, and available APIs/feeds.