from functools import lru_cache

from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input as preprocesar_mobilenet
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input as preprocesar_resnet

from utilidades.imagenes import cargar_imagen_desde_bytes, convertir_imagen_a_arreglo


def normalizar_nombre_modelo(nombre_modelo: str) -> str:
    nombre_limpio = nombre_modelo.strip().lower()
    if nombre_limpio == "resnet50":
        return "ResNet50"
    return "MobileNetV2"


@lru_cache(maxsize=2)
def cargar_modelo_preentrenado(nombre_modelo: str):
    if nombre_modelo == "ResNet50":
        return ResNet50(weights="imagenet")
    return MobileNetV2(weights="imagenet")


def preprocesar_para_modelo(arreglo_imagen, nombre_modelo: str):
    if nombre_modelo == "ResNet50":
        return preprocesar_resnet(arreglo_imagen)
    return preprocesar_mobilenet(arreglo_imagen)


def predecir_imagen(contenido_imagen: bytes, nombre_modelo: str) -> dict:
    modelo_seleccionado = normalizar_nombre_modelo(nombre_modelo)
    modelo_preentrenado = cargar_modelo_preentrenado(modelo_seleccionado)

    imagen = cargar_imagen_desde_bytes(contenido_imagen)
    arreglo_imagen = convertir_imagen_a_arreglo(imagen)
    imagen_procesada = preprocesar_para_modelo(arreglo_imagen, modelo_seleccionado)

    predicciones_modelo = modelo_preentrenado.predict(imagen_procesada)
    predicciones_decodificadas = decode_predictions(predicciones_modelo, top=5)[0]

    predicciones = [
        {
            "clase": nombre_clase,
            "porcentaje_confianza": float(probabilidad * 100),
        }
        for _, nombre_clase, probabilidad in predicciones_decodificadas
    ]

    return {
        "modelo": modelo_seleccionado,
        "predicciones": predicciones,
    }
