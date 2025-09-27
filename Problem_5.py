# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Teorema Fundamental de la Aritmética para encontrar el MCM entre dos números.
#   1. Descomponer en factores primos
#   2. Identificar la mayor potencia.
#   3. Multiplicar las potencias.




# Problema 3:
def factores_primos(n): 
    factores_primos = []
    primo = 2
    while n > 1:
        if n % primo == 0:
            factores_primos.append(primo)
            n = n/primo
        else:
            primo += 1
    return factores_primos

for i in range(2,21):
    f = factores_primos(i)
    print(f)


# Lo encuentra pero tarda mucho tiempo.
# n = 1
# div = []
# while len(div) < 20:
#    div = []
#    for i in range (1, 21):
#        if n % i == 0:
#            div.append(i)
#    n += 1
# print(div)