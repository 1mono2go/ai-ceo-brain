CREATE TABLE ai_ceo_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMP DEFAULT now(),
    query TEXT,
    decision JSONB,
    sensitivity TEXT
);
