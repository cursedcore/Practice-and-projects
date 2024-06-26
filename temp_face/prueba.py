import cv2

#Cargar las imagenes
image_to_detect = cv2.imread('images/fr.jpg')

#Checar si la imagen se está mostrando correctamente
cv2.imshow("prueba",image_to_detect)