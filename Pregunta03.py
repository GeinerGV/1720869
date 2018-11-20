from os import system
system("cls")
n = 0
while n<=0:
    try:
        n = int(input("Ingrese el orden N de la matriz (N x N) a operar: >> "))
    except Exception:
        pass
    finally:
        system("cls")

print("Matriz generada ("+str(n)+" x "+str(n)+"):\n")

from random import random
from math import pow

def generarMatiz(num):
    matriz = []
    for i in range(num):
        matriz.append([])
        for j in range(num):
            matriz[i].append(int((random()+0.5)*(i+j+2)*(pow(-1,int((i+j)*random())))))
    return matriz

def prinMatriz(matriz):
    for i in matriz:
        print(i)

def sumaDiagonalPrincipal(matriz):
    suma = 0
    for i in range(len(M)):
        suma += M[i][i]
    return suma

M = generarMatiz(n)

prinMatriz(M)

print("\nLa suma de la diagonal principal de la matriz generada es:", sumaDiagonalPrincipal(M), "\n")