import os
from pathlib import Path
from typing import Optional
from uuid import uuid4


def guardar_imagen_analizada(contenido_imagen: bytes, nombre_archivo: Optional[str]) -> str:
    carpeta_imagenes = Path(os.getenv("IMAGE_UPLOAD_DIR", "imagenes_analizadas"))
    carpeta_imagenes.mkdir(parents=True, exist_ok=True)

    extension = Path(nombre_archivo or "imagen.jpg").suffix.lower()
    if extension not in {".jpg", ".jpeg", ".png", ".webp", ".bmp"}:
        extension = ".jpg"

    ruta_imagen = carpeta_imagenes / f"{uuid4().hex}{extension}"
    ruta_imagen.write_bytes(contenido_imagen)
    return str(ruta_imagen)
