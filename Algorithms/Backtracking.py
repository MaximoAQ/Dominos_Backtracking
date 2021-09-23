from Helpers.misc import swap, verify

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Algoritmo de resolucion de tablero dominosa haciendo uso del Backtracking
#
# @param pBoard = Matriz sobre el cual se ejecutara el algoritmo para la busqueda de
#                   soluciones
# @param pTiles = Lista de fichas que sera utilizada para verificaciones
# @param pSolution = Posible solucion a verificar
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
listaFichas     = []
listaIndices    = []

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
def compViejo(sol,pre):
    sol = reductor(sol,pre)
    if (sol == pre):
        return True
    return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

solActual   = [] #Aqui se almacenaran los valores que han sido leidos de la solucion que se este leyendo
listaSol    = [] #Aqui se colocaran las distintas combinaciones ya probadas, para poder hacer la poda

#Recibe 2 listas, la solucion que se va a leer y el prefijo de la lista
#de soluciones que fallaron
def comparador(sol,pre):
    value = True
    for i in range(0,len(pre)):
        if pre[i]!=sol[i]:
            return False
    return value

#Pasa un int a lista
def intToList(num):
    if (type(num)==int):
        lista = []
        lista = [int(i) for i in str(num)]
        return lista

#Cuano el algoritmo haya escrito la solucion que lee y esta falla, la mete en la lista de soluciones malas
def agregarSol():
    global solActual
    global listaSol
    if (solActual.size() != 0)
        listaSol.append(solActual)
        solActual = []


def backtracking(pBoard,pTiles, pSolution):
    global listaSol
    global solActual

    # @var tile_holder = variable para guardar las fichas a buscar
    tile_holder = [] 
    
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

                            # Agrega la orientacion de la ficha a la lista de solucion actual
                            solActual.append(0)
                        
                        #Si existe un error de indice esto significa que la solucion no es valida
                        except IndexError:
                            solActual.append(0)
                            agregarSol()
                            return False

                    # Si la posicion 0 de la solucion es un 1, esto significa que se va a leer una ficha de forma Vertical
                    elif(pSolution[0] == 1):
                        try:
                            #Se agrega la coordenada leida y la de abajo inmediata a tile_holder
                            tile_holder.append(pBoard[i][j])
                            tile_holder.append(pBoard[i+1][j])

                            # Las coordenadas leidas se convierten en string para marcar que ya se leyeron
                            pBoard[i][j] = str(pBoard[i][j])
                            pBoard[i+1][j] = str(pBoard[i+1][j])

                            # Agrega la orientacion de la ficha a la lista de solucion actual
                            solActual.append(1)

                        #Si existe un error de indice esto significa que la solucion no es valida    
                        except IndexError:
                            solActual.append(1)
                            agregarSol()
                            return False

                    # Se verifica si la pieza de tile_holder existe en la lista de piezas 
                    if(verify(tile_holder, pTiles)):

                        # Se hace el intento de remover la pieza de la lista donde se busca, si falla se le da la vuelta y se vuelve a intentar
                        try:
                            pTiles.remove(tile_holder)
    
                        except:
                            swap(tile_holder)
                            pTiles.remove(tile_holder)
                        
                        # Se hace la llamada recursiva eliminando el paso actual de la solucion
                        return brute_force(pBoard, pTiles, pSolution[1:])
                    
                    #Si no existe en la lista se asume que ya se coloco por lo tanto la solucion no es valida
                    else:
                        return False








