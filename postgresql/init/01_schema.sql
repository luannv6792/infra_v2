-- ===============================
-- CORE ENTITIES
-- ===============================

CREATE TABLE IF NOT EXISTS application (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS environment (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS deployment (
    id BIGSERIAL PRIMARY KEY,
    application_id INT REFERENCES application(id),
    environment_id INT REFERENCES environment(id),
    deploy_time TIMESTAMP NOT NULL,
    status TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_deployment_time
ON deployment(deploy_time);
