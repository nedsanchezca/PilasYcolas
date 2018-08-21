import csv
import libro 
import pila as pilita

pilaLibros = pilita.Pila()
pilaEncontrados = pilita.Pila()
pilaAuxiliar = pilita.Pila()

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
        if pilaLibros.es_vacia:
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
    contador = len(pilaEncontrados.items)
    while contador != 0:
        libroAux = pilaEncontrados.desapilar()
        print("Autor Obra: " + libroAux.autor + " Titulo Obra: " + libroAux.titulo)
        contador = contador - 1
        if contador == 0:
            break

#Arranque del programa
print("Cómo desea buscar el libro")
print("\n1. Por género \n2. Por autor")
opcion = input("Digite la opción correspondiente: ")
if(opcion==str(1)):
    atributo = input("Digite el género del libro: ")
    buscarGenero(atributo)
elif (opcion==str(2)):
    atributo = input("Digite el autor del libro: ")
    buscarAutor(atributo)
else:
    print("Digite una opción correcta")

imprimirPila()
