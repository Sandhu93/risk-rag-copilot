CREATE TABLE IF NOT EXISTS exposures (
    id SERIAL PRIMARY KEY,
    counterparty TEXT NOT NULL,
    exposure_usd BIGINT NOT NULL,
    as_of_date DATE NOT NULL,
    risk_bucket TEXT NOT NULL
);

INSERT INTO exposures (counterparty, exposure_usd, as_of_date, risk_bucket)
VALUES
    ('ABC Capital', 12000000, '2026-01-31', 'high'),
    ('Zenith Bank', 9500000, '2026-01-31', 'medium'),
    ('NorthStar Holdings', 6100000, '2026-01-31', 'low')
ON CONFLICT DO NOTHING;
