from Helpers.misc import swap, verify

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Algoritmo de resolucion de tablero dominosa haciendo uso del Backtracking
#
# @param pBoard = Matriz sobre el cual se ejecutara el algoritmo para la busqueda de
#                   soluciones
# @param pTiles = Lista de fichas que sera utilizada para verificaciones
# @param pSolution = Posible solucion a verificar
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

listaFichas = []
listaIndices = []

#Genera una lista con listas que representan cada ficha ej: [[0,0],[0,1],[1,1]]
def generarDominos(n):
    global listaFichas
    n+=1
    for i in range(0,n):
        for j in range (i,n):
                listaFichas +=[[i,j]]
    return lista

def generarTabla(n):
	global listaIndices
	total = (n-1)*(n+2)
	total += 1
    for i in range(0,total):
    	listaIndices += [False]


def backtracking(pBoard,pTiles, pSolution):
	missingTiles = []

	# Si ya no hay fichas ni pasos en la solucion significa que todas fueron asignadas
    # Pero si quedan fichas y ya no hay pasos significa que no fue una solucion valida
    if pTiles == [] and pSolution == []:
        return True
    elif(pTiles!=[] and pSolution == []):
        return False
    else:
        # Se usan 2 for para recorrer la matriz de izquierda a derecha, de arriba a abajo
        for i in range(len(pBoard)):
            for j in range(len(pBoard[i])):








