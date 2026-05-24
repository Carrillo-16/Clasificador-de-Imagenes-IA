from io import BytesIO

import numpy as np
from PIL import Image


def cargar_imagen_desde_bytes(contenido_imagen: bytes) -> Image.Image:
    try:
        imagen = Image.open(BytesIO(contenido_imagen)).convert("RGB")
        imagen.load()
        return imagen
    except Exception as error:
        raise ValueError("El archivo no contiene una imagen valida") from error


def convertir_imagen_a_arreglo(imagen: Image.Image, tamano_imagen: tuple[int, int] = (224, 224)) -> np.ndarray:
    imagen_redimensionada = imagen.resize(tamano_imagen)
    arreglo_imagen = np.array(imagen_redimensionada, dtype=np.float32)
    imagen_procesada = np.expand_dims(arreglo_imagen, axis=0)
    return imagen_procesada
