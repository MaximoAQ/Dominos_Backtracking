import random

from Clases.GameNode import Game_Node
from Table_gen.dominoes import make_tiles
from Algorithms.BruteForce import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Funcion de lectura de archivos de Tablero
#
# @param num = numero de archivo a leer
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_file(num):

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

def solucion_gen(num):
    solution = []
    for i in range(num):
        solution.append(random.randint(0,1))
    return solution


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Funcion principal del programa 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    N = 4
    Fichas = make_tiles(N)
    Solution_Size = len(Fichas)

    read_file(N)
    print(solucion_gen(Solution_Size))

    #brute_force(Tablero, Fichas)


if __name__ == "__main__":
    #@var Board = variable global donde se guarda la matriz a tablero a trabajar
    #@var Tiles = variable global donde se guardan las fichas determinadas por tdNum 
    #@var Solutions = Matriz de posibles soluciones
    Board = []
    Tiles = []
    
    #Llamada a funcion princial del programa
    main()