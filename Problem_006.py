# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ⋯ + 10^2 = 385.
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ⋯ + 10)^2 = 55^2 = 3025.
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

# Se crea una variable en la que iremos sumando los numeros al cuadrado del 1
# al 100.
sum_sq = 0

# Se crea un ciclo que recorrerá todos estos números.
for i in range (1, 101):

     # Eleva al cuadrado este número "i" en el que esté la iteración y se lo
     # suma a la variable que habíamos creado para guardad la suma total.
     sum_sq += i**2

# Se crea una variable en la cual iremos sumando los números del 1 al 100, una
# suma simple de los números naturales hasta el 100.
suma = 0

# Ciclo que recorre todos los números naturales hasta el 100.
for i in range (1, 101):

     # Aquí irá sumando cada uno de los números que vaya recorriendo este
     # ciclo.
     suma += i

# La suma total de los números naturales hasta el 100 se eleva al cuadrado y
# se guarda en una variable nueva.
sq_sum = suma**2

# Imprime la suma de la diferencia entre la suma de los cuadrados y la suma al
# cuadrado.
print(sq_sum - sum_sq)