# Problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or
# 5 below 1000.


# Este código lo que hace es crear una variable a la que le iremos sumanndo
# los números que sean múltiplos de 3 o 5.
suma = 0

# Recorre los números del 1 al 999 (debajo de 1000).
for i in range(1,1000):

    # Si el número "i" de la iteración actual es divisible entre 3 o 5, sin
    # residuo, lo toma como verdadero.
    if (i % 3 == 0) or (i % 5 == 0):

        # Si el número "i" logra pasar el condicional pasado, entonces se suma
        # a la variable que habíamos guardado en la cual íbamos a ir sumando
        # estos números encontrados (múltiplo de 3 o 5).
        suma += i

# Imprime el resultado final, el cual debería ser la suma de todos los
# múltiplos de 3 o 5, menores a 1000.
print(suma)