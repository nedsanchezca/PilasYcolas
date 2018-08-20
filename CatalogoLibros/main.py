import csv
import libro 
import pila

pilaLibros = pila.Pila()
pilaEncontrados = pila.Pila()
pilaAuxiliar = pila.Pila()

'''Procedemos a guardar en la pila los objetos de libros con los parametros dados por el archivo'''
with open('libros.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        linea = row[0]
        lineaSeparada = linea.split(";")
        objetoAux = libro.Libro(lineaSeparada[0], lineaSeparada[2], lineaSeparada[1])
        pilaLibros.apilar(objetoAux)
        linea = ""


def buscarAutor(parametro):
    while pilaLibros.es_vacia != 0:
        librito = pilaLibros.desapilar()
        if librito.autor == parametro:
            pilaEncontrados.apilar(librito)
        else:
            pilaAuxiliar.apilar(librito)
        if pilaLibros.es_vacia():
            break

def buscarGenero(parametro):
    while pilaLibros.es_vacia != 0:
        librito = pilaLibros.desapilar()
        if librito.genero == parametro:
            pilaEncontrados.apilar(librito)
        else:
            pilaAuxiliar.apilar(librito)
        if pilaLibros.es_vacia():
            break

def imprimirPila():
    libroAux = pilaEncontrados.desapilar()
    print(libroAux.autor + " + " + libroAux.titulo)

#Arranque del programa
print("Cómo desea buscar el libro")
print("\n1. Por género \n2. Por autor")
opcion = input("Digite la opción correspondiente")
if(opcion==str(1)):
    atributo = input("Digite el género del libro")
    buscarAutor(atributo)
elif (opcion==str(2)):
    atributo = input("Digite el autor del libro")
    buscarGenero(atributo)
else:
    print("Digite una opción correcta")

imprimirPila()
