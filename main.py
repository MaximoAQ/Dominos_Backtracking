from Helpers.misc import binary_increment, read_file, solucion_gen, binlistToInt, reductorListas,busquedaBinaria
from Table_gen.dominoes import make_tiles, place_tile
from Algorithms.BruteForce import *
from copy import deepcopy
from Algorithms.Backtracking import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Funcion principal del programa 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    N = 5
    Tiles = make_tiles(N)
    Solution_Size = len(Tiles)
    posible_sol = solucion_gen(Solution_Size)
    sol_list = []

    read_file(Board, N)

    for i in range(2**Solution_Size):
        workBoard = deepcopy(Board)
        workTiles = deepcopy(Tiles)
        
        if(brute_force(workBoard, workTiles, posible_sol)):
            sol_list.append(deepcopy(posible_sol))
            print(posible_sol)
        
        binary_increment(posible_sol)
        
    print(sol_list)

def mainBack():
    N = 3
    Tiles = make_tiles(N)
    Solution_Size = len(Tiles)
    posible_sol = solucion_gen(Solution_Size)
    sol_list = []
    flag = True

    read_file(Board, N)

    for i in range(2**Solution_Size):
        workBoard = deepcopy(Board)
        workTiles = deepcopy(Tiles)

        if flag:
            backtracking(workBoard, workTiles, posible_sol)
            flag = False

        x = binlistToInt(posible_sol)
        if not(busquedaBinaria(listaBinaria,x)):
        #for i in range(0,len(listaSol)):
            #x = binlistToInt(reductorListas(posible_sol,listaSol[i]))
            #y = binlistToInt(listaSol[i])
            #if not (comparador(posible_sol,listaSol[i])):
           # if (z!=y):
            if(backtracking(workBoard, workTiles, posible_sol)):
                sol_list.append(deepcopy(posible_sol))
                print(posible_sol)
        
        binary_increment(posible_sol)

        if (len(sol_list)>=1):
            return sol_list[0]
    print(sol_list)


if __name__ == "__main__":
    #@var Board = variable global donde se guarda la matriz a tablero a trabajar
    #@var Tiles = variable global donde se guardan las fichas determinadas por tdNum 
    Board = []
    Tiles = []

    #Llamada a funcion princial del programa
    mainBack()