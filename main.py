
def brute_force():
    print(Tablero)
    return

def main(tdNum):
    #Variable de tablero global para poder utilizarla en otros metodos
    global Tablero
    Tablero = []

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
    for line in lines[2:]:
        if line == '':
            break
        Tablero.append(line.split(" ")[:-1])
    
    return


if __name__ == "__main__":
    main(1)
    brute_force()