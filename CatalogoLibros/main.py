import csv
#import pila.py

#pila1 = pila()

with open('libros.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rowToDivide = str(row[0])
        rowToDivide.split(';')
        print(rowToDivide)