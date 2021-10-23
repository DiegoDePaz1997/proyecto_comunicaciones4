import cv2
import pytesseract
import time as t

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'



class texto:


    def __init__(self):
        self.texto = ''
        self.condicion = False
        self.recorte = ''
        self.redundancia_numero = 0


    def redundanica_numero(self, numero):
        if self.redundancia_numero == numero:
            self.redundancia_numero == 0
            return True
        else:
            self.redundancia_numero = numero
            return False


    def ingreso(self, text):
        self.texto = text


    def __condiciones(self, cont):
        esta = lambda x: str(x) in '1234567890'

        if esta(self.texto[cont]) : 
                if  esta(self.texto[cont+1]) and esta(self.texto[cont+2]) and esta(self.texto[cont+3]):  
                    #print(strs[cont: cont+4])
                    return True
                else: 
                    return False


    def busqueda_numeros_consecutivos(self):

        '''se ingresa una cadena y se verifica si hay 4 numeros consecutivos
            si los hay devuelve desde el primero hasta 15 posiciones despues'''

        for i in range(len(self.texto)):
            if self. __condiciones(i):   
                condi =  self. __condiciones(i + 5) and  self. __condiciones(i + 11)
                
                if condi:
                    self.recorte = self.texto[i: i+15]
                    self.condicion = True
                    break# <====== le faltaba el break, pase como 40 mins pensando proque no funcionaba
                    
                else:
                    self.condicion = False




class video:


    def __init__(self):
        self.vid = cv2.VideoCapture(0)
        self.frame = 0
        self.frame_tratado = 0
        self.recorte_de_frame = 0
        self.cond = False


    def toma_frame(self):
        _, self.frame = self.vid.read()


    def umbral_de_frame(self):
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        ret,self.frame_tratado = cv2.threshold(gray, 190, 255 , cv2.THRESH_BINARY)


    def contornos(self):
        contours,_ = cv2.findContours(self.frame_tratado,
                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        for c in contours:
            if cv2.contourArea(c)>5500:
                cv2.drawContours(self.frame, c, -1, (0, 0, 255), 2, cv2.LINE_AA)

                x,y,w,h = cv2.boundingRect(c)
                self.recorte_de_frame = self.frame[y:y+h, x:x+w]
                return True
                
        return False


    def colocar_texto(self, texto):
        texto = 'DPI = '+ texto
        ubicacion = (100, 240)
        font = cv2.FONT_HERSHEY_TRIPLEX
        tamanoLetra = 1
        colorLetra = (255,0,0)
        grosorLetra = 1
        cv2.putText(self.frame, texto, ubicacion, font, tamanoLetra, colorLetra, grosorLetra)


    def mostrar_frame(self):
        cv2.imshow('frame', self.frame)
        #cv2.imshow('recorte', self.recorte_de_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   self.cond = True


    def terminar(self):
        self.vid.release()
        cv2.destroyAllWindows()




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

                

        video.mostrar_frame()
        if video.cond: break

    video.terminar()
