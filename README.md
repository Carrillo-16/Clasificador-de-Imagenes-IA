# Clasificador de Imagenes IA

Sistema academico de clasificacion general de imagenes con FastAPI, TensorFlow/Keras, React, TypeScript, PostgreSQL y SQLAlchemy.

El usuario carga una imagen desde la interfaz web, selecciona MobileNetV2 o ResNet50, y el backend devuelve el TOP 5 de clases ImageNet con porcentajes de confianza. La API guarda cada prediccion en PostgreSQL junto con la ruta de la imagen analizada, el modelo usado y la fecha.

## Despliegue completo

Con Docker instalado, levanta PostgreSQL, backend y frontend con:

```bash
docker compose up --build
```

Servicios:

- Frontend: `http://127.0.0.1:8080`
- Backend: `http://127.0.0.1:8000`
- Health check: `http://127.0.0.1:8000/salud`
- PostgreSQL: `127.0.0.1:5432`

Credenciales locales de PostgreSQL:

- Host: `127.0.0.1`
- Puerto: `5432`
- Base de datos: `clasificador_imagenes_ia`
- Usuario: `clasificador_app`
- Contrasena: `ClasificadorIA2026Local`
- URL SQLAlchemy: `postgresql+psycopg://clasificador_app:ClasificadorIA2026Local@localhost:5432/clasificador_imagenes_ia`

Si no usas Docker, crea la base con PostgreSQL local:

```bash
psql -U postgres -f scripts/crear_postgresql.sql
```

## Backend

Requiere Python 3.11.

```bash
cd BACKENDIA
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:aplicacion --reload --host 0.0.0.0 --port 8000
```

El backend lee configuracion desde `BACKENDIA/.env`. La plantilla versionable esta en `BACKENDIA/.env.example`.

Endpoint principal:

```text
POST http://127.0.0.1:8000/predecir
```

Campos esperados:

- `imagen`: archivo de imagen.
- `nombre_modelo`: `MobileNetV2` o `ResNet50`.
- `nombre_usuario`: opcional.
- `correo_usuario`: opcional.

## Frontend

```bash
cd FRONTENDIA
npm install
npm run dev
```

La interfaz de desarrollo queda en `http://127.0.0.1:5173`.

El frontend lee `VITE_API_URL` desde `FRONTENDIA/.env`. En desarrollo apunta a `http://127.0.0.1:8000`; en Docker/Nginx se usa `/api`.

## Notas operativas

- TensorFlow puede descargar pesos oficiales de ImageNet durante la primera prediccion.
- Las imagenes subidas se guardan en `BACKENDIA/imagenes_analizadas` o en el volumen Docker `imagenes_analizadas`.
- La API rechaza archivos que no sean imagenes y limita cada subida a 8 MB por defecto.
