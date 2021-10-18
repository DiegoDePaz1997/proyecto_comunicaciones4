import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def numeros_consecutivos(strs):

    '''se ingresa una cadena y se verifica si hay 4 numeros consecutivos
        si los hay devuelve desde el primero hasta 15 posiciones despues'''

    esta = lambda x: str(x) in '1234567890'

    def condiciones(cont):
        if esta(strs[cont]) : 
                if  esta(strs[cont+1]) and esta(strs[cont+2]) and esta(strs[cont+3]):   
                    #print(strs[cont: cont+4])
                    return True
                else: 
                    return False


    for i in range(len(strs)):
        if condiciones(i):
            condi = condiciones(i + 5) and condiciones(i + 11)

            if condi:
                return strs[i: i+15]

    return False

  


def contornos(frame, frame_humbral):
    contours,_ = cv2.findContours(frame_humbral,
                     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   

    for c in contours:
        if cv2.contourArea(c)>5500:
            cv2.drawContours(frame, c, -1, (0, 0, 255), 2, cv2.LINE_AA)

            x,y,w,h = cv2.boundingRect(c)
            ROI = frame[y:y+h, x:x+w]
            return True, ROI
            #
    return False, False






def video(vid):
    '''lee imagen a imagen y extrae el texto que encuentre
        retorna el texto '''
    
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray, 190, 255 , cv2.THRESH_BINARY)
    
    texto = 'texto' 
    cond_recorte, recorte = contornos(frame, thresh)
    if cond_recorte: texto = pytesseract.image_to_string(recorte, config='--psm 11')
    
    #cv2.imshow('roi', recorte)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True , texto   
    else: return False, texto





def redundancia_dpi(lista_de_redund_dpi, texto):
    '''
    Se ingresa una lista  y un texto se guarda en la lista las veces
    necesarias, luego se verifica si todos los valores son iguales
    
    '''

    if numeros_consecutivos(texto):
        lista_de_redund_dpi.append(numeros_consecutivos(texto))


    if len(lista_de_redund_dpi)>2:
            lis = True
            for i in lista_de_redund_dpi:
                lis &= lista_de_redund_dpi[0] == i 
                print(lis)
                   

            if lis:
                print('NUM_DPI', numeros_consecutivos(texto))
                del lista_de_redund_dpi[:]

            else:
                        
                del lista_de_redund_dpi[:]




if __name__=='__main__':
    pass


        
