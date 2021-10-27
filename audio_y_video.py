from video_texto import *
from audio import primera_o_segunda_dosis, cambio_dpi
from base_de_datos import *
import time as t

    #seleccionar primera hoja
def nomYapellido(texto):
    return ''.join([i for i in texto if i in 'ABCDEFGHIJKLMNÑOPQRSTUVWYXZ'])


if __name__=='__main__':
    video = video()
    text = texto()
    update_data()

    while True:
        video.toma_frame()

        


            #lo mas lento es la busqueda con pytesseract
        texto_tess = pytesseract.image_to_string(video.frame, config='--psm 11')
        text.ingreso(texto_tess)
        text.busqueda_numeros_consecutivos()

    


        if text.condicion :
            video.colocar_texto(text.recorte)
            video.mostrar_frame()
            text.condicion = False
            cambio_dpi([text.recorte])

            primera_o_segunda_dosis()
            f_datos()



                

        video.mostrar_frame()
        if video.cond: break

    video.terminar()
