
CREATE TABLE IF NOT EXISTS hello (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

INSERT INTO hello(message)
SELECT 'Hello from PostgreSQL'
WHERE NOT EXISTS (SELECT 1 FROM hello);
