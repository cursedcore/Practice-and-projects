#importar las librerias
import cv2
import face_recognition

#Cargar las imagenes
image_to_detect = cv2.imread('images/nombre-img.jpg')

#Checar si la imagen se está mostrando correctamente
#cv2.imshow("prueba",image_to_detect)

#Lo siguiente es encontrar y imprimir la cantidad de caras a reconocer

#Encuentra las localizaciones de las caras usando la funcion face_locations()
#el modelo de reconocimiento puede ser cnn o hog
#number_of_times_to_upsample=1  Por predeterminado la funcion detecta un rostro pero si aumentamos el numero, la cantidad de rostros a detectar aumenta

all_face_locations = face_recognition.face_locations(image_to_detect, model='hog')

#Imprimir el numero de rostros detectados
#el modelo de reconocimiento es mas rapido, si usamos cnn tarda mucho mas en cargar
print('Aqui hay {} numero de rostros detectados en esta imagen'.format(len(all_face_locations)))

#Encontrar la posicion de las caras en una imagen (nota la imagen sera tomada como una matriz)

for index, current_face_location in enumerate(all_face_locations):
    top_pos,right_pos,bottom_pos,left_pos = current_face_location
    print('Se encontro la cara {} en top {} right {} bottom {} left {}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))

    #cortar la imagen de la cara
    current_face_image =image_to_detect[top_pos:bottom_pos,left_pos:right_pos]
    #Mostrar en una ventana las imagenes de las caras detectadas
    cv2.imshow("Cara num:"+str(index+1),current_face_image)