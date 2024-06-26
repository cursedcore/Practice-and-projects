# MK Ultra 35
                        #### Video Demo: https://youtu.be/7Eqanul08i0
                        #### Description:
                           App Model ->
                           Este script de Python utiliza las bibliotecas OpenCV y face_recognition para realizar el reconocimiento facial en tiempo real a partir de un video capturado desde la cámara web. A continuación, se detalla el funcionamiento paso a paso:

                           1. Importación de librerías:
                              - Se importan las librerías necesarias, como `cv2` (OpenCV) para el procesamiento de imágenes y `face_recognition` para el reconocimiento facial.

                           2. Captura de video:
                              - Se inicializa la captura de video desde la cámara web mediante la función `cv2.VideoCapture(0)` y se almacena en la variable `webcam_video_stream`.

                           3. Carga de imágenes y obtención de embeddings:
                              - Se cargan las imágenes de muestra de las personas a reconocer y se obtienen los embeddings faciales correspondientes utilizando la función `face_recognition.face_encodings()`.
                              - Cada imagen tiene asociado un conjunto de encodings (representación numérica del rostro) que permiten identificar y comparar los rostros en tiempo real.

                           4. Inicialización de arreglos:
                              - Se inicializan los arreglos `all_face_locations`, `all_face_encodings` y `all_face_names` para almacenar la ubicación de los rostros detectados, los encodings de los rostros y los nombres correspondientes respectivamente.

                           5. Procesamiento del video:
                              - Se inicia un bucle infinito para procesar cada frame del video capturado desde la cámara web.
                              - Se lee el frame actual mediante `webcam_video_stream.read()` y se almacena en `current_frame`.
                              - Se reduce el tamaño del frame para reducir el consumo de recursos utilizando `cv2.resize()`.
                              - Se detectan todas las caras presentes en el frame utilizando `face_recognition.face_locations()`.
                              - Se obtienen los encodings faciales para cada cara detectada mediante `face_recognition.face_encodings()`.

                           6. Comparación y reconocimiento de caras:
                              - Se recorren las localizaciones y los encodings faciales obtenidos en el paso anterior utilizando un bucle `for`.
                              - Se cambia la magnitud de las posiciones para que concuerden con el tamaño real del frame.
                              - Se realiza una comparación de los encodings faciales con los encodings de las imágenes de muestra utilizando `face_recognition.compare_faces()`.
                              - Si se encuentra una coincidencia, se obtiene el índice de la primera coincidencia verdadera (`True`) y se recupera el nombre de la persona correspondiente desde el arreglo `known_face_names`.

                           7. Dibujado de rectángulos y etiquetas:
                              - Se dibuja un rectángulo alrededor de la cara detectada utilizando `cv2.rectangle()`.
                              - Se muestra el nombre de la persona reconocida como texto en la imagen utilizando `cv2.putText()`.

                           8. Reconocimiento de género:
                              - Se extrae la porción de la imagen que contiene el rostro actual utilizando los valores de posición obtenidos en el paso anterior.
                              - Se crea un objeto `blob` a partir de la imagen del rostro actual utilizando `cv2.dnn.blobFromImage()`.
                              - Se utiliza un modelo preentrenado para predecir el género del rostro actual.
                              - Se muestra el género como texto en la imagen utilizando `cv2.putText()`.

                           9. Mostrar video procesado:
                              - Se muestra el video procesado con los rectángulos y las

                           etiquetas dibujadas mediante `cv2.imshow()`.
                              - Si se presiona la tecla 'q', se interrumpe el bucle y se finaliza la ejecución del script.

                           10. Liberación de recursos:
                              - Una vez finalizado el bucle, se libera el video capturado y se cierran todas las ventanas de OpenCV mediante `webcam_video_stream.release()` y `cv2.destroyAllWindows()` respectivamente.

                           Este script permite realizar reconocimiento facial en tiempo real utilizando la cámara web y mostrar los resultados en pantalla, incluyendo la detección de caras, el reconocimiento de personas conocidas y la predicción del género de las caras detectadas.

                           Web Page -> Importaciones:

                           secrets es utilizado para generar una clave secreta aleatoria que se utiliza como clave de sesión.
                           Flask es el framework utilizado para construir la aplicación web.
                           redirect, render_template, request, session y url_for son funciones y objetos proporcionados por Flask para manejar las rutas y vistas de la aplicación.
                           sqlite3 se utiliza para interactuar con la base de datos SQLite donde se almacenan los datos de usuarios y psets.
                           datetime se utiliza para obtener la fecha y hora actual.
                           Configuración de la aplicación:

                           Se crea una instancia de la aplicación Flask.
                           Se genera una clave secreta utilizando secrets.token_hex(32).
                           La clave secreta se establece como clave secreta de la aplicación Flask para la gestión de sesiones.
                           Rutas:

                           /: La ruta de inicio que muestra la página de inicio. Si el usuario ha iniciado sesión, muestra un saludo personalizado.
                           /logout: La ruta para cerrar sesión. Elimina el nombre de usuario almacenado en la sesión y redirige a la página de inicio.
                           /login: La ruta para iniciar sesión. Si se envía un formulario con las credenciales de inicio de sesión, verifica las credenciales en la base de datos y establece el nombre de usuario en la sesión. Si las credenciales son válidas, redirige a la página de inicio; de lo contrario, muestra un mensaje de error.
                           /contacto: La ruta que muestra la página de contacto.
                           /informacion: La ruta que muestra la página de información.
                           /registro: La ruta para registrar nuevos usuarios. Si se envía un formulario con los datos de registro, verifica si el correo electrónico ya está registrado y, si no, inserta los datos del usuario en la base de datos. Si el registro es exitoso, redirige a la página de inicio; de lo contrario, muestra un mensaje de error.
                           /inicio: La ruta que muestra los psets relacionados con el usuario que ha iniciado sesión. Obtiene el ID del usuario de la sesión y recupera los psets correspondientes de la base de datos.
                           /vencimiento: La ruta que muestra los psets vencidos relacionados con el usuario que ha iniciado sesión. Obtiene el ID del usuario de la sesión y recupera los psets correspondientes de la base de datos utilizando una condición específica.
                           /realizados: La ruta que muestra los psets completados relacionados con el usuario que ha iniciado sesión. Obtiene el ID del usuario de la sesión y recupera los psets correspondientes de la base de datos utilizando una condición específica.
                           /crear: La ruta para crear un nuevo pset. Si se envía un formulario con los detalles del pset, se inserta en la base de datos y se redirige a la página de inicio.
                           Funciones de manejo de rutas:

                           index(): Verifica si el nombre de usuario está almacenado en la sesión y muestra la página de inicio con un saludo personalizado si está presente.
                           logout(): Elimina el nombre de usuario almacenado en la sesión y redirige a la página de inicio.
                           login(): Maneja el inicio de sesión. Verifica las credenciales en la base de datos y establece el nombre de usuario en la sesión si son válidas. Redirige a la página de inicio en caso de éxito; de lo contrario, muestra un mensaje de error.
                           contacto(): Muestra la página de contacto.
                           informacion(): Muestra la página de información.
                           registro(): Maneja el registro de nuevos usuarios. Verifica si el correo electrónico ya está registrado y, si no, inserta los datos del usuario en la base de datos. Redirige a la página de inicio en caso de éxito; de lo contrario, muestra un mensaje de error.
                           inicio(): Muestra los psets relacionados con el usuario que ha iniciado sesión. Obtiene el ID del usuario de la sesión y recupera los psets correspondientes de la base de datos.
                           vencimiento(): Muestra los psets vencidos relacionados con el usuario que ha iniciado sesión. Obtiene el ID del usuario de la sesión y recupera los psets correspondientes de la base de datos utilizando una condición específica.
                           realizados(): Muestra los psets completados relacionados con el usuario que ha iniciado sesión. Obtiene el ID del usuario de la sesión y recupera los psets correspondientes de la base de datos utilizando una condición específica.
                           crear(): Maneja la creación de un nuevo pset. Inserta los detalles del pset en la base de datos y redirige a la página de inicio.
                           Ejecución de la aplicación:

                           El código final ejecuta la aplicación Flask.

                           En resumen, el código proporciona una aplicación web básica con funcionalidades de inicio de sesión, registro de usuarios y gestión de psets. Utiliza una base de datos SQLite para almacenar la información de los usuarios y los psets.

