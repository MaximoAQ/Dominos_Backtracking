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
listaSoluciones = [] #Aqui se colocaran las distintas combinaciones ya probadas, para poder hacer la poda

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
    for i in range(0,total):
    	listaIndices += [False]
    return listaIndices

# Convierte a el int de solucion(sol) del mismo largo que el de prefijo(pre)
def reductor(sol,pre):
    listaPre = list(str(pre))
    listaSol = list(str(sol))
    
    while(len(listaSol)>len(listaPre)):
        listaSol.pop(-1)

    sol = int("".join(listaSol))  
    return  sol

#Sol representa la solucion que se le esta pasando
#Mientras que pre, es el prefijo de la lista que no funciono
def comparador(sol,pre):
    sol = reductor(sol,pre)
    if (sol == pre):
        return True
    return False


def backtracking(pBoard,pTiles, pSolution):
	missingTiles = []

	# Si ya no hay fichas ni pasos en la solucion significa que todas fueron asignadas
    # Pero si quedan fichas y ya no hay pasos significa que no fue una solucion valida
    if pTiles == [] and pSolution == []:
        return True
    elif(pTiles!=[] and pSolution == []):
        return False

    else:
        for i in range(len(pBoard)):
            for j in range(len(pBoard[i])):



            	# Se pregunta si lo que se esta leyendo en la matriz es un entero
                if(isinstance(pBoard[i][j], int)):

                    # Si la posicion 0 de la solucion es un 0, esto significa que se va a leer una ficha de forma Horizontal
                    if(pSolution[0] == 0):
                        try:
                            #Se agrega la coordenada leida y la derecha inmediata a tile_holder
                            tile_holder.append(pBoard[i][j])
                            tile_holder.append(pBoard[i][j+1])

                            # Las coordenadas leidas se convierten en string para marcar que ya se leyeron
                            pBoard[i][j] = str(pBoard[i][j])
                            pBoard[i][j+1] = str(pBoard[i][j+1])
                        
                        #Si existe un error de indice esto significa que la solucion no es valida
                        except IndexError:
                            return False








