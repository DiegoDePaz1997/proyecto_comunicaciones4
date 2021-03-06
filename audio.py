import speech_recognition as sr
import pyttsx3
import random as ran
from datetime import datetime




num_dpi = [14873]

list_data = []

r = sr.Recognizer() 
engine = pyttsx3.init() 
hoy = datetime.now()



def cambio_dpi(dpi):
    global num_dpi
    num_dpi = dpi




def return_datos():
    return list_data.pop()






def speakText(command):   
    engine.say(command)
    engine.runAndWait()



def escucha():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=.2)
        print('Speak Anything : ')
        audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio, language='en-ES')
            print('palabras: {}'.format(text))
            speakText(text)
            return text.lower()
        except:
            speakText('error')
            return 'Nac'


def rec_aproximado(texto, lista):
    '''
    con almenos la mitad de las letras iguales
    se acepta el texto como igual a uno de la lista
    '''

    for tex_evaluar in lista:
        aux = 0
           
        for letra_texto, letra_ev in zip(texto,tex_evaluar):
            if letra_texto == letra_ev:
                aux += 1

            if aux/len(texto)> .4 :    return tex_evaluar

    return False



def modulo_a_dirigirse():
    modulo = ('primer', 'segundo', 'tercero', 'cuarto', 'quinto')
    mod_aleatorio = ran.choice(modulo)
    speakText(f'dirigirse al {mod_aleatorio} modulo')
    return mod_aleatorio + ' modulo'



def fecha_de_vacunacion():
    speakText('en que mes la recibio')
    lista = ('enero', 'febrero', 'marzo', 'abril', 'mayo',
            'julio', 'junio', 'agosto', 'septiembre',
            'octubre', 'noviembre', 'diciembre',
            
            'january', 'february', 'march', 'april',
            'may','june','july','august','september', 
            'october' ,'november' ,'december' ) 

    while True:
        texto = escucha()
        palabra = rec_aproximado(texto, lista)
        if palabra:
             speakText(f'muy bien, {palabra}')
             return palabra
        else:  
            speakText('podria repetirlo')



def tipo_de_vacuna():
    dic ={ 'uno':'pfizer', 'dos':'sputnik', 'tres':'moderna'}
    speakText('que vacuna le pusieron')
    speakText('diga la posicion de la vacuna')
    speakText('pfizer 1. sputnik 2. moderna 3')

    while True:
        texto = escucha()
        palabra = rec_aproximado(texto, dic.keys())

        if palabra:
            speakText(f'muy bien, {dic[palabra]}')
            return dic[palabra]
        else:
            speakText('podria repetirlo')





def mes_vacunacion(num):
    lista = ('enero', 'febrero', 'marzo', 'abril', 'mayo',
            'julio', 'junio', 'agosto', 'septiembre',
            'octubre', 'noviembre', 'diciembre') 
    return   lista[num-1]






def primera_Vacuna():
    speakText('primera vacuna')   
    modulo= modulo_a_dirigirse()
    list_data.append(num_dpi + ['primera vacuna',mes_vacunacion(hoy.month),'sputnik', modulo])




def segunda_Vacuna():
    fecha = fecha_de_vacunacion()
    vacuna_tipo = tipo_de_vacuna()
    modulo = modulo_a_dirigirse()
    list_data.append(num_dpi+ ['segunda vacuna', fecha, vacuna_tipo, modulo])

    
    
 

def primera_o_segunda_dosis():
    lista = ['primera','segunda']
    speakText('es su primera o segunda dosis') 

    while True:
        texto = rec_aproximado(escucha(), lista)

        
        if texto == 'primera':
            primera_Vacuna()
            break
        elif texto == 'segunda':
            segunda_Vacuna()
            break
        else:
            speakText('ninguna se reconocio')
            speakText('podria repetirlo')







if __name__ == '__main__':
    primera_o_segunda_dosis()
   
