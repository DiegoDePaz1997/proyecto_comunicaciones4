import gspread
from audio import return_datos
from audio import *
gc = gspread.service_account(filename='glass-arcana-329906-0ac43598603c.json')
#abrir por titulo


sh = gc.open('base de datos')
    #seleccionar primera hoja
worksheet = sh.get_worksheet(0)


dic = {}


    


def add_dic(iN, fin):
    for i in range(iN, fin):
        lista = worksheet.row_values(i)
        dic[lista[0]] = lista[1:]  
  


def update_data():
    tamano_dic = len(dic)
    val = int(worksheet.acell('H1').value)

    if tamano_dic == 0 and val > 0: #bajo la base de datos 
             add_dic(2, val+1)



def envio_datos(lista):
    dic[lista[0]] = lista[1:]
    val = int(worksheet.acell('H1').value)
    idd = val+2
    worksheet.update(f'A{idd}:E{idd}', [lista])
    worksheet.update('H1', val + 1)



def f_datos():
    print('hola mundo')
    lista = return_datos()
    print(lista)

    update_data()
    envio_datos(lista)






