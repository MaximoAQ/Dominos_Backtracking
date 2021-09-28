#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Funcion de lectura de archivos de Tablero
#
# @param num = numero de archivo a leer
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_file(Board, num):

    #Abre el archivo y lo lee, si no lo encuentra devuelve un mensaje y cierra el programa
    try:
        with open('Table_gen/TableroDoble'+str(num)+'.txt') as tdFile:
            lines = tdFile.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].replace("\n","")
    except:
        print('No se encontro el tablero')
        return

    #inserta los valores del tablero del archivo en una matriz para poder utilizarla posteriormente
    
    for line in lines[2:]:
        if line == '':
            break
        holder = []

        for item in (line.split(" ")[:-1]):
            holder.append(int(item))

        Board.append(holder)
    return



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Funcion para verificar si una ficha se encuentra en la lista de fichas, prueba 
# ambas posiciones [1|0] y [0|1]
#
# @param pPair = Ficha por verificar
# @param pList = Lista de fichas donde se busca la ficha a verificar
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def verify(pPair, pList):
    if(pPair in pList):
        return True
    else:
        swap(pPair)
        return pPair in pList

def swap(pPair):
    pPair[0], pPair[1] = pPair[1], pPair[0]
    return 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Funcion generadora de soluciones para algoritmo de fuerza bruta
#
# @param num = Cantidad de digitos de la posible solucion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def solucion_gen(num):
    solution = []
    for i in range(num):
        solution.append(0)
    return solution

def binary_increment(bin):
    
    for i in range(1,len(bin)+1):
        if(bin[-i]) == 0:
            bin[-i] = 1
            return
        else:
            bin[-i] = 0
    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def listToInt(lista):
    strings = [str(integer) for integer in lista]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer

def binlistToInt(binary):
    number = 0
    for b in binary:
        number = (2 * number) + b
    return number

def reductorListas(sol,pre):
    newSol=[]
    if (len(pre)<=len(sol)):
        for i in range(0,len(pre)):
            newSol.append(sol[i])
        return newSol
    else:
        return sol

def busquedaBinaria(unaLista, item):
    primero = 0
    ultimo = len(unaLista)-1
    encontrado = False

    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)//2
        if unaLista[puntoMedio] == item:
            encontrado = True
        else:
            if item < unaLista[puntoMedio]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1

    return encontrado


def dominosaArr(size, array):
    filas = []
    matriz = []
    while (True):
        for i in range(0, size + 2):
            filas.append(array[i])

        matriz.append(filas)
        del array[:size + 2]
        filas = []

        if len(array) < (size + 2):
            break

    return matriz