from video_texto import *
from audio import primera_o_segunda_dosis, imprecion_datos_por_audio, cambio_dpi



if __name__=='__main__':
    video = video()
    text = texto()

    while True:
        video.toma_frame()
        video.umbral_de_frame() 
        
        cond_recorte = video.contornos()
        if cond_recorte: 
            #lo mas lento es la busqueda con pytesseract
            texto_tess = pytesseract.image_to_string(video.recorte_de_frame, config='--psm 11')
            text.ingreso(texto_tess)
            text.busqueda_numeros_consecutivos()


            if text.condicion and text.redundanica_numero( text.recorte):
                video.colocar_texto(text.recorte)
                video.mostrar_frame()
                text.condicion = False
                cambio_dpi(text.recorte)
                primera_o_segunda_dosis()
                imprecion_datos_por_audio()

                

        video.mostrar_frame()
        if video.cond: break

    video.terminar()
