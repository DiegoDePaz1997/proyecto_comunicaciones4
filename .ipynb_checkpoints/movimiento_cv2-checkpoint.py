import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

stss = 'C:/Users/diego/Documentos/Python/cosas/lab_com4/'
ima = '3.png'


imagen = cv2.imread(stss + ima)



#cambia el espacio de color, solo gris
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(gray, 3)
#umbral, lo que este entre los parametros pasan
#canny = cv2.Canny(gray,150,250)
#canny = cv2.dilate(canny,None,iterations=1)
_, canny = cv2.threshold(median,100,255,cv2.THRESH_BINARY)


contornos2, hierrarchy2 = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)





salida = 0
for c in contornos2:
    area = cv2.contourArea(c)    
    if(area > 3000):
        x, y, w, h = cv2.boundingRect(c)
        cv2.drawContours(imagen, c, -1, (0, 255,0), 3)
        dpi = gray[y:y+h, x:x+w]

        
proporcion_img = dpi.shape
alto, ancho = proporcion_img
num_dpi = dpi[20*alto//100:30*alto//100, 2*ancho//100 : 37*ancho//100]
texto = pytesseract.image_to_string(num_dpi, config='--psm 11')
print('NUM_DPI', texto)



cv2.putText(imagen, f'num dpi={texto}', (x-20, y-10), 1, 2.2, (0, 255,0),3)
cv2.imshow('imagen', imagen)
cv2.imshow('dpi', num_dpi)




cv2.waitKey(0)
cv2.destroyAllWindows()


