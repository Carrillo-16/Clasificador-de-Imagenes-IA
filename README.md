Clasificador-de-Imagenes-IA

Repositorio para el sistema de clasificación de imágenes con transferencia de aprendizaje para la clase de inteligencia artificial IA, ingeniería en sistemas.

Este proyecto corresponde a un sistema académico de clasificación general de imágenes. Su propósito es permitir que un usuario cargue una imagen desde una interfaz web y obtenga una predicción automática utilizando modelos de inteligencia artificial preentrenados.

El sistema está dividido en dos partes principales. El backend se encuentra en la carpeta BACKENDIA y contiene la API desarrollada con Python y FastAPI. El frontend se encuentra en la carpeta FRONTENDIA y contiene la interfaz web desarrollada con React, TypeScript y Axios.

El backend utiliza TensorFlow y Keras para cargar modelos preentrenados sobre ImageNet. Esto permite reconocer categorías generales sin necesidad de entrenar un dataset personalizado. Entre las categorías que el sistema puede reconocer se encuentran animales, vehículos, objetos, alimentos, herramientas, tecnología, prendas de vestir y muchas otras clases incluidas en ImageNet.

Los modelos incluidos son MobileNetV2 y ResNet50. Ambos modelos se cargan con pesos preentrenados de ImageNet. MobileNetV2 es un modelo ligero y eficiente, adecuado para predicciones rápidas y equipos con recursos limitados. ResNet50 es un modelo más profundo, con mayor capacidad de representación, útil para comparar resultados y analizar diferencias entre arquitecturas.

Cuando el usuario sube una imagen, el backend procesa el archivo, adapta el tamaño de la imagen al formato esperado por el modelo seleccionado, ejecuta la predicción y obtiene las cinco clases más probables. La respuesta incluye el nombre de la clase detectada y su porcentaje de confianza.

La base de datos utilizada es SQLite mediante SQLAlchemy. El sistema guarda información de la imagen analizada, el modelo utilizado, la predicción principal, el porcentaje de confianza y la fecha de la predicción. SQLite se utiliza por su simplicidad y porque no requiere instalación adicional, lo cual lo hace adecuado para un proyecto académico. La estructura está preparada para que posteriormente pueda migrarse a otro motor de base de datos si fuera necesario.

El frontend permite seleccionar el modelo, cargar una imagen, ejecutar la predicción y visualizar el resultado. También incluye la opción de comparar MobileNetV2 y ResNet50 usando la misma imagen, mostrando los resultados principales de cada modelo.

Este repositorio no incluye dependencias pesadas ni archivos generados localmente. No se suben carpetas como venv, node_modules, dist, bases de datos SQLite generadas, imágenes analizadas ni archivos temporales. Esto mantiene el repositorio limpio, liviano y fácil de clonar.

Para ejecutar el backend después de descargar el proyecto, se deben instalar las dependencias en un entorno virtual de Python. Se recomienda usar Python 3.11 porque TensorFlow estable puede presentar problemas con versiones más recientes como Python 3.13 o Python 3.14.

Comandos para instalar el backend
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Comando para levantar el backend
venv\Scripts\activate
uvicorn main:aplicacion --reload

También puede ejecutarse sin activar manualmente el entorno virtual usando este comando
venv\Scripts\python.exe -m uvicorn main:aplicacion --reload

La API quedará disponible en la siguiente dirección
http://127.0.0.1:8000

Para ejecutar el frontend después de descargar el proyecto, se deben instalar las dependencias de Node.js.

Comandos para instalar el frontend
npm install

Comando para levantar el frontend
npm run dev

La interfaz web quedará disponible normalmente en la siguiente dirección
http://127.0.0.1:5173

Para usar el sistema completo, primero debe estar ejecutándose el backend y luego el frontend. Después de abrir la interfaz web, se puede cargar una imagen, seleccionar un modelo y ejecutar la predicción. Si se usa la opción de comparación, el sistema enviará la misma imagen a MobileNetV2 y ResNet50 para mostrar los resultados de ambos modelos.

Durante la primera ejecución, TensorFlow puede descargar automáticamente los pesos oficiales de ImageNet para MobileNetV2 y ResNet50 si todavía no existen en la caché local del equipo. Esto es normal y solo ocurre la primera vez que se cargan los modelos.

El objetivo de este repositorio es servir como respaldo y base de mejora continua para el sistema de clasificación de imágenes. La estructura separada de backend y frontend permite mantener el proyecto organizado, comprensible y fácil de ampliar.
