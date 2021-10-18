import func_text_imagen as mov
import cv2
#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
lista_de_redund_dpi = []









# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
      
    estado, texto =    mov.video(vid)
    mov.redundancia_dpi(lista_de_redund_dpi, texto)  

    if estado : break







# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()







