import sys

lista = [i for i in range(100_000)]
print(sum(lista))
print(sys.getsizeof(lista), 'bytes')
listaa = (i for i in range(100_000))
print(sum(listaa))
print(sys.getsizeof(listaa), 'bytes')



name: str
num: int = 10
num = 'hola'
print(num)

def facebook(procesos) -> None:
    for i in range(procesos): 
        yield print(f'pross F No: {i}')



def TikTok(procesos):
    for i in range(procesos): 
        yield print(f'pross Tik No: {i}')


    

def googlear():
    print('que es python')
    yield 
    print('que es una variable')
    yield 
    print('que es asignacion de variables')
    yield 
    print('que es una condicional')
    yield 
    print('que es un bucle')
    yield



    
x = 0
F = facebook(5)
T = TikTok(5)
while x<5:
    next(F)
    next(T)
    next(googlear())
    x+=1

cond = True

x = 'es verdad' if cond else 'es falso'
print(x)

def cons(c):
    return 'es verdad' if c else 'es falso'

print(cons(False))


cadena = 'hola esto es solo un moton de letras sin importancia como hola year \
            tampoco tiene sentido solo es para hacerla una lista'

lista = cadena.split()
'''muy interesante, devuelve una lista con las posiciones de todas las
coincidencias  de e'''
busqueda = [i for i,e in enumerate(lista) if e == 'solo']
print(busqueda)



def bucle(texto):
    while True:
        if texto =='salir': break
        print(f'mensaje enviado = {texto}')
        yield 


lista = 'esto es un texto y me pela salir puto'.split()
for letras in lista:
    next(bucle(letras))
