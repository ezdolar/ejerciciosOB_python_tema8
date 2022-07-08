def main():
    archivoEscritura = open('archivo.txt', 'w')
    textoEscrito = 'Hola\nmundo\nfeliz!'
    archivoEscritura.write(textoEscrito)
    archivoEscritura.close()

    archivoLectura = open('archivo.txt', 'r')
    textoLeido = archivoLectura.read()
    print(textoLeido)

if __name__ == '__main__':
    main()