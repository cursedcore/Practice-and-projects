import cv2
import face_recognition

original_image=cv2.imread('images/testing/modi.jpg')

#Cargar embeddings de las muestras de las imagenes
sample_image = face_recognition.load_image_file('dir/sample.img')
sample_encoding= face_recognition.face_encoding(sample_image)[0]
                                                    #0 debido a que se supone que solo se busca una cara
#crear un array donde se guarden los encoding de las imagenes
known_face_encodings=[sample_encoding]
#array para guardar el nombre de las personas
known_face_names["Ejemploxd"]

#Imagen para reconocer las caras
image_to_recognize= face_recognition.load_image_image("Direccion")

all_face_locations = face_recognition.face_locations(image_to_recognize,model='hog')
all_face_encodings = face_recognition.face_encodings(image_to_recognize,all_face_locations)


#Cicla a traves de los embeds de la cara desconocida
for current_face_locations, current_face_enconding in zip(all_face_locations_all_face_encondings):
    #Cortar  la tupla para obtener el valor de las 4 posiciones de la cara
    top_pos, right_pos, bottom_pos, left_pos = currennt_face_location

    all_matches=face_recognition.compare_faces(known_face_encondings,current_face_encoding)


    #Label para la cara desconocida
    name_of_person = 'unknown_face'

    #Verificar si las coincidencias contienen almenos un item
    #de ser verdadero, obten el indice de la cara que esta localizada en el indice de all_matches
    if True in all_matches:
        first_match_index=all_matches.index(True)
        name_of_person=known_face_names[first_match_index]

    #Dibujar rectangulo
     cv2.rectangle(original_image, (left_pos, top_pos),(right_pos, bottom_pos), (255, 0, 255), 2)

    font= cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(original_image,name_of_person, (left_pos,bottom_pos),font,0.5,(255,255,255),1)

    cv2.imshow('Caras identificadas',original_image)