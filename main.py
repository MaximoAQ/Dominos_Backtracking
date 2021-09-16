from Helpers.misc import binary_increment, read_file, solucion_gen
from Table_gen.dominoes import make_tiles
from Algorithms.BruteForce import *





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Funcion principal del programa 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    N = 5
    Fichas = make_tiles(N)
    Solution_Size = len(Fichas)
    posible_sol = solucion_gen(Solution_Size)

    for i in range(18):
        print(posible_sol)
        binary_increment(posible_sol)


    read_file(Board, N)
    print(Board)

    #brute_force(Tablero, Fichas)


if __name__ == "__main__":
    #@var Board = variable global donde se guarda la matriz a tablero a trabajar
    #@var Tiles = variable global donde se guardan las fichas determinadas por tdNum 
    Board = []
    Tiles = []

    #Llamada a funcion princial del programa
    main()