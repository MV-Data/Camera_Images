import streamlit as st
from PIL import Image


# Ruta de la imagen en formato JPG o PNG
ruta_imagen = "C:/Workspace_proyectos/Curso_Python_20_apps/app1/Bonus/travesti.png"


#Empieza la camara
camera_image = st.camera_input("Camera")

if camera_image:

    #Creo una instancia de Pillow
    img =  Image.open(camera_image)

    #Convierto la imagen a escala de grises
    gray_img = img.convert('L')

    #Renderizo la imagen en escala de grises en la webpage
    st.text("mejorando imagen....")
    st.image(gray_img)
    st.text("mejorando imagen, aguarde, esta jodido....")
    travesti = Image.open(ruta_imagen)
    st.image(travesti)
    st.text("Es lo mejor que pudimos hacer....")