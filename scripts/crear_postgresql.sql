-- Ejecutar como usuario administrador de PostgreSQL, por ejemplo:
-- psql -U postgres -f scripts/crear_postgresql.sql

DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'clasificador_app') THEN
        CREATE USER clasificador_app WITH PASSWORD 'ClasificadorIA2026Local';
    END IF;
END
$$;

SELECT 'CREATE DATABASE clasificador_imagenes_ia OWNER clasificador_app'
WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'clasificador_imagenes_ia')\gexec

GRANT ALL PRIVILEGES ON DATABASE clasificador_imagenes_ia TO clasificador_app;
