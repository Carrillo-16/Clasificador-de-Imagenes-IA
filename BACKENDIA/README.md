---
title: Clasificador Imagenes Backend
colorFrom: blue
colorTo: gray
sdk: docker
app_port: 8000
pinned: false
---

# Backend Clasificador General de Imagenes

API academica con FastAPI, TensorFlow/Keras, SQLAlchemy y PostgreSQL.

## Instalacion

Usar Python 3.11.

```bash
cd BACKENDIA
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar

```bash
uvicorn main:aplicacion --reload --host 0.0.0.0 --port 8000
```

Rutas:

- `GET /`
- `GET /salud`
- `POST /predecir`

## Base de datos

PostgreSQL local:

- Usuario: `clasificador_app`
- Contrasena: `ClasificadorIA2026Local`
- Base de datos: `clasificador_imagenes_ia`
- URL: `postgresql+psycopg://clasificador_app:ClasificadorIA2026Local@localhost:5432/clasificador_imagenes_ia`

La configuracion se cambia con `DATABASE_URL` en `.env`.

## Modelos

- MobileNetV2 con `weights="imagenet"`
- ResNet50 con `weights="imagenet"`

La primera ejecucion puede descargar pesos oficiales de Keras si no existen en cache local.
