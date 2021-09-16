from Helpers.misc import swap, verify

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Algoritmo de resolucion de tablero domino haciendo uso de la fuerza bruta
#
# @param pBoard = Matriz sobre el cual se ejecutara el algoritmo para la busqueda de
#                   soluciones
# @param pTiles = Lista de fichas que sera utilizada para verificaciones
# @param pSolution = Posible solucion a verificar
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def brute_force(pBoard, pTiles, pSolution):
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
                        
                        #Si existe un error de indice esto significa que la solucion no es valida
                        except IndexError:
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

                        #Si existe un error de indice esto significa que la solucion no es valida    
                        except IndexError:
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