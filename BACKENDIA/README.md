# Clasificador General de Imagenes con ImageNet

Proyecto academico simple con FastAPI, TensorFlow/Keras, SQLAlchemy y SQLite.

El sistema usa modelos preentrenados sobre ImageNet, por lo que no necesita dataset personalizado ni entrenamiento manual.

## Ruta backend

`C:\Users\default.DESKTOP-CNVIP6E\Desktop\Proyectos\IA\BACKENDIA`

## Modelos incluidos

- MobileNetV2 con `weights="imagenet"`
- ResNet50 con `weights="imagenet"`

La primera ejecucion puede descargar pesos oficiales de Keras si no existen en cache local.

## Instalacion backend

Usar Python 3.11. El equipo tiene Python 3.14 instalado, pero TensorFlow estable no es compatible con esa version.

```bash
cd C:\Users\default.DESKTOP-CNVIP6E\Desktop\Proyectos\IA\BACKENDIA
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar API

```bash
cd C:\Users\default.DESKTOP-CNVIP6E\Desktop\Proyectos\IA\BACKENDIA
venv\Scripts\activate
uvicorn main:aplicacion --reload
```

Otra forma equivalente sin activar manualmente el entorno:

```bash
cd C:\Users\default.DESKTOP-CNVIP6E\Desktop\Proyectos\IA\BACKENDIA
venv\Scripts\python.exe -m uvicorn main:aplicacion --reload
```

Endpoint principal:

```text
POST http://127.0.0.1:8000/predecir
```

Campos esperados:

- `imagen`: archivo de imagen.
- `nombre_modelo`: `MobileNetV2` o `ResNet50`.

Respuesta esperada:

```json
{
  "modelo": "MobileNetV2",
  "predicciones": [
    {
      "clase": "golden_retriever",
      "confianza": "95.00%"
    }
  ]
}
```

## Base de datos

El proyecto usa SQLite por defecto:

```text
clasificador_imagenes.db
```

Se guarda la ruta de la imagen analizada, el modelo usado, la prediccion principal, el porcentaje de confianza y la fecha.

Las imagenes subidas se almacenan localmente en:

```text
imagenes_analizadas/
```

Para migrar despues a SQL Server, cambia `URL_BASE_DATOS` en `base_datos/conexion.py`.
