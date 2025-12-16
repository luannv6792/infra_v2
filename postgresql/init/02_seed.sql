INSERT INTO environment(name)
VALUES ('sit'), ('uat'), ('stg'), ('prod')
ON CONFLICT DO NOTHING;

INSERT INTO application(name)
VALUES ('demo-app')
ON CONFLICT DO NOTHING;
