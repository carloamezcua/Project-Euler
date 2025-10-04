# Problem 4:
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit number is
# 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.



# Se crean dos listas (m y n), cada una con tres elementos que corresponden a
# las centenas, decenas y unidades. 
m = [9, 0, 0]
n = [9, 0, 0]

# Se crea una lista vacía donde iremos guardando los número palíndromos que
# vayamos encontrando.
palindromo = []

# En esta parte anidamos cuatro ciclos "for", esto es para comprobar si es
# palíndromo en cada una de las combinaciones posibles intercambiando los
# valores de las decenas y unidades de ambas listas. Dejamos las centenas
# fijas en 9 ya que buscamos el número palíndromo dado de la multiplicación de
# dos números de tres dígitos, esto con el fin de evitar todas las
# combinaciones posibles que incluían centenas menores de nueve, ya que estos
# palíndromos serán menores que los resultantes de los que tienen el valor
# nueve en las centenas.
for k in range(10):
    m[1] = k
    for l in range(10):
        m[2] = l
        for i in range(10):
            n[1] = i
            for j in range(10):
                n[2] = j

                # Se juntan los elemntos de la lista en un solo valor "int".
                # Esto se hace para las listas "m" y "n".
                M = int(str(m[0]) + str(m[1]) + str(m[2]))
                N = int(str(n[0]) + str(n[1]) + str(n[2]))

                # Se multiplica la combinación correspondiente a la iteración
                # actual en la que se encuentre.
                R = M * N

                # Convertimos a "sring" la multiplicación de estos dos números
                # para poder comparar sus elementos y saber si es palíndromo.
                R_str = str(R)

                # Si es número que pasamos a strig es igual si lo leemos al
                # derecho y al revés. Entonces es palíndromo y pasa.
                if R_str == R_str[::-1]:

                    # El número que pasó la condición es un palíndromo,
                    # estonces lo agregamos a la lista que creamos para
                    # guardar estos números.
                    palindromo.append(R)

# Imprime el valor máximo de la lista palíndromo una vez que termina de hacer
# todas las combinaciones. Esta lista tendra dos palíndromos iguales porque
# incluye los casos A*B y B*A.
print(max(palindromo))