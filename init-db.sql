CREATE TABLE IF NOT EXISTS ejemplo (
	id SERIAL PRIMARY KEY,
	mensaje TEXT NOT NULL
);

INSERT INTO ejemplo (mensaje) VALUES ('Primeros pasos de test');
