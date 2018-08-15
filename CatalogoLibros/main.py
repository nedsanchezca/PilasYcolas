import csv
#import pila.py

#pila1 = pila()

with open('libros.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        linea = row[0]
        lineaSeparada = linea.split(";")
        print(lineaSeparada)
