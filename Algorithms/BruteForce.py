#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Algoritmo de resolucion de tablero domino haciendo uso de la fuerza bruta
#
# @param pTablero = Matriz sobre el cual se ejecutara el algoritmo para la busqueda de
#                   soluciones
# @param pFichas = Lista de fichas que sera utilizada para verificaciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def brute_force(pTablero, pFichas):
    result_array = []
    chip_holder = []


    for i in range(len(pTablero)):
        print(pTablero[i])
        for j in range(len(pTablero[i])):
            if (isinstance(pTablero[i][j], str)):
                print("chocobaby")
            else:
                try:
                    chip_holder.append(pTablero[i][j])
                    chip_holder.append(pTablero[i][j+1])
                    pTablero[i][j] = str(pTablero[i][j])
                    pTablero[i][j+1] = str(pTablero[i][j+1])

                    
                except:
                    print("pero vamo a ver, terrible")

                    
                
        
        
    

    
    for i in pTablero:
        print(i)
    # print(Fichas)
    print(chip_holder)

    return