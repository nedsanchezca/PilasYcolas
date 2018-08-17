import csv
import libro 
import pila

pilaLibros = pila.Pila()
pilaEncontrados = pila.Pila()
pilaAuxiliar = pila.Pila()

with open('libros.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        linea = row[0]
        lineaSeparada = linea.split(";")
        objetoAux = libro.Libro(lineaSeparada[0], lineaSeparada[2], lineaSeparada[1])
        pilaLibros.apilar(objetoAux)
    
    while pilaLibros.es_vacia != 0:
        print(pilaLibros.items[0].autor)
        pilaLibros.desapilar()
