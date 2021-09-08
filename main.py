from Table_gen.dominoes import make_tiles
def brute_force():
    print("Tablero: ", Tablero)
    print("Fichas: ", Fichas)
    return

def main(tdNum):
    #@var Tablero = variable global donde se guarda la matriz a tablero a trabajar
    #@var Fichas = variable global donde se guardan las fichas determinadas por tdNum 
    global Tablero
    global Fichas
    Tablero = []
    Fichas = []

    #Abre el archivo y lo lee, si no lo encuentra devuelve un mensaje y cierra el programa
    try:
        with open('Table_gen/TableroDoble'+str(tdNum)+'.txt') as tdFile:
            lines = tdFile.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].replace("\n","")
    except:
        print('No se encontro el tablero')
        return

    #inserta los valores del tablero del archivo en una matriz para poder utilizarla posteriormente
    Fichas = make_tiles(int(lines[0]))
    for line in lines[2:]:
        if line == '':
            break
        Tablero.append(line.split(" ")[:-1])
    
    return


if __name__ == "__main__":
    main(2)
    brute_force()