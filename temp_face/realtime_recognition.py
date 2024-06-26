import cv2
import face_recognition

# Captura el video de la camara predeterminada (camara integrada)
webcam_video_stream = cv2.VideoCapture(0)
# Aumentar el indice de videocapture hace que se cambie de camara en caso de haber mas de una

# Iniciar un arreglo para almacenar las localizaciones en cada fotograma
all_face_locations = []

# Crear un ciclo que recorra cada fotograma
# ret es un booleano que indicara si el fotograma se leyó correctamente
while True:
    ret, current_frame = webcam_video_stream.read()
    # Reducir 1/4 del tamaño del fotograma para procesamiento menos pesado
    current_frame_small = cv2.resize(current_frame, (0, 0), fx=0.25, fy=0.25)
    # Encontrar el numero de caras a reconocer
    all_face_locations = face_recognition.face_locations(current_frame_small, number_of_times_to_upsample = 2, model='hog')

    for index, current_face_location in enumerate(all_face_locations):
        top_pos, right_pos, bottom_pos, left_pos = current_face_location

        # Se debe multiplicar las posiciones para compensar con el reajuste de tamaño y que vaya de acuerdo con el fotograma minimizadp
        top_pos *= 4
        right_pos *= 4
        bottom_pos *= 4
        left_pos *= 4

        # Dibujar el rectangulo alrededor de la cara
        # el primer argumento es el frame, el segundo y tercer argumento son tuplas indicando posciones, el cuarto es el color del tectangulo y el quinto es el grosor
        cv2.rectangle(current_frame, (left_pos, top_pos),
                      (right_pos, bottom_pos), (0, 0, 255), 2)

        print('Se encontro la cara {} en top {} right {} bottom {} left {}'.format(
            index+1, top_pos, right_pos, bottom_pos, left_pos))
        # Mostrar la cara con el rectangulo dibujado
        # Debido a la naturaleza de la condicion del for, los fotogramas dejaran de mostrarse si
        # Se tapa la cara o sale de la vista de la camara, para evitar esto, solo hay que sacar el imshow del ciclo for y dejarlo dentro del ciclo while
        cv2.imshow("Video Webcam", current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos de la camara una vez se haya roto el ciclo while
webcam_video_stream.release()
cv2.destroyAllWindows()
