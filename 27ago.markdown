## 27 de agosto
Se logró identificar que antes de tratar de calcular la dimensión fractal de una imagen, necesitamos aislar el objeto de interés.
Hay varias técnicas para aislar objetos de interés, en general se engloban en el área de visión computacional.
Ejemplos de ello son detección de bordes, análisis espectral de colores, análisis estadístico simple, etc.

El **siguiente paso** para resolver esta tarea (medir la dimensión fractal de las palmeras) es detectar sus bordes. (ponerlas en "blanco y negro", blanco lo que queremos medir, las palmeras, y negro el "fondo", lo demás).
No hay que perder de vista el problema de investigación a resolver: caracterizar objetos de interés desde imágenes y/o video desde drones, postes, etc.

Nuestro interés por un problema de investigación para este curso, más que los detalles de una solución (programas, por ejemplo), es el distinguir los problemas importantes que se necesitan resolver para llevar a una solución final y definir la metodología (trazar la ruta a seguir) de investigación.
Subiré al sitio web del curso un programa para calcular dimensión fractal por cajas en python.

## Bibliografía a revisar:

* Ejemplo pequeño en Python para localizar un objeto con cierto contraste, dentro de una imagen general.
  * https://stackoverflow.com/questions/14767594/how-to-detect-object-on-images
* Detección de bordes básica
border detection – Python's eyes
  * https://pythoneyes.wordpress.com/tag/border-detection/
* Biblioteca avanzada con diferentes algoritmos de visión por computadora.

  * OpenCV
    * https://opencv.org
  * OpenCV: OpenCV modules
    * https://docs.opencv.org/4.1.1/index.html