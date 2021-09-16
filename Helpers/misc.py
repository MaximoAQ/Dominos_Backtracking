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
        pPair[0], pPair[1] = pPair[1], pPair[0]
        return pPair in pList


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
    
    for i in range(1,len(bin)):
        if(bin[-i]) == 0:
            bin[-i] = 1
            return
        else:
            bin[-i] = 0
    return