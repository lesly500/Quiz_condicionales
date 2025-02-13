# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = int(input("Poner valor a: "))
b = int(input("Valor b: "))
c = int(input("Poner valor c: "))

# processing
if (a+b > c) or (a+c >  b) or (b+c > a):
    #Output
    print("No se puede formar.")
else:
    print("Puede formar un triangulo. ")
pass
