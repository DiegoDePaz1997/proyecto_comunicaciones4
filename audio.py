import speech_recognition as sr
import pyttsx3
import random as ran
from datetime import datetime

num_dpi = 1923423
dic_general_de_datos = {}
list_data = []

r = sr.Recognizer() 
engine = pyttsx3.init() 
hoy = datetime.now()


def cambio_dpi(dpi):
    global num_dpi
    num_dpi = dpi




def imprecion_datos_por_audio():
    print('----'*25)
    for i,j in dic_general_de_datos.items():
        
        print(f'dpi = {i} \ndatos = {j}  \n ' )
        print('----'*25)


def speakText(command):   
    engine.say(command)
    engine.runAndWait()



def escucha():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=.5)
        print('Speak Anything : ')
        audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
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

            if aux/len(texto)> .3 : return tex_evaluar
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
    dic ={ 'primera':'pfizer', 'segunda':'sputnik', 'tercera':'moderna'}
    speakText('que vacuna le pusieron')
    speakText('diga la posicion de la vacuna')
    speakText('pfizer primera. sputnik segunda. moderna tercera')
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


def guardado_datos():
        dic_general_de_datos[num_dpi] = list_data.pop()





def primera_Vacuna():
    speakText('primera vacuna')   
    modulo= modulo_a_dirigirse()
    list_data.append(['primera vacuna',mes_vacunacion(hoy.month),'sputnik', modulo])
    guardado_datos()



def segunda_Vacuna():
    fecha = fecha_de_vacunacion()
    vacuna_tipo = tipo_de_vacuna()
    modulo = modulo_a_dirigirse()
    list_data.append(['segunda vacuna', fecha, vacuna_tipo, modulo])
    guardado_datos()
    
    
 

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
    #primera_o_segunda_dosis()
    dic = {'2320 55634 0103': ['primera vacuna', 'octubre', 'sputnik', 'cuarto modulo'], '3002 03276 0101': ['segunda vacuna', 'febrero', 'pfizer', 'cuarto modulo']}
    print('----'*25)
    for i,j in dic.items():
        
        print(f'dpi = {i} \ndatos = {j}  \n ' )
        print('----'*25)
 
