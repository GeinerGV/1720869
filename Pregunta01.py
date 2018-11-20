x = None
y = None
from os import system
system("cls")
while x==None or y==None:
    try:
        if x==None:
            x = int(input("Ingrese el valor de x >> "))
        else:
            print("x:", x)
            y = int(input("Ingrese el valor de y >> "))
    except Exception:
        pass
    finally:
        system("cls")
print("C1: (", x, ";", y, ")")
print("C0: (0; 0)\n")

from math import hypot, trunc

distacia = trunc(hypot(x, y))

print("La distancia entre C0 y C1 es:", distacia, "\n")