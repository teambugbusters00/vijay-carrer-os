CREATE TABLE IF NOT EXISTS jobs (
  id BIGSERIAL PRIMARY KEY,
  source TEXT NOT NULL,
  external_id TEXT,
  company TEXT NOT NULL,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  location TEXT,
  remote_status TEXT,
  eligibility TEXT,
  eligibility_reason TEXT,
  compensation TEXT,
  experience TEXT,
  skills JSONB DEFAULT '[]',
  description TEXT,
  posted_at TIMESTAMPTZ,
  deadline TIMESTAMPTZ,
  fit_score NUMERIC,
  first_seen TIMESTAMPTZ DEFAULT NOW(),
  last_seen TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(source, url)
);

CREATE TABLE IF NOT EXISTS applications (
  id BIGSERIAL PRIMARY KEY,
  job_id BIGINT REFERENCES jobs(id),
  status TEXT NOT NULL DEFAULT 'discovered',
  generated_material JSONB DEFAULT '{}',
  approved_at TIMESTAMPTZ,
  submitted_at TIMESTAMPTZ,
  notes TEXT
);
