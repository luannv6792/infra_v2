CREATE OR REPLACE VIEW deployment_today AS
SELECT
    a.name AS application,
    e.name AS environment,
    COUNT(*) AS total
FROM deployment d
JOIN application a ON d.application_id = a.id
JOIN environment e ON d.environment_id = e.id
WHERE d.deploy_time::date = CURRENT_DATE
GROUP BY a.name, e.name;
