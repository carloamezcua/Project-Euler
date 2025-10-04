# Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# El problema se resolvió factorizando el número "n". Aquí creamos una lista
# vacía para ir guardando los factores primos. 
factores_primos = []

# Se crea una variable que guarda el número que queremos factorizar, después
# se modificará. 
n = 600851475143

# Primer número primo, después comenzará a sumar de 1 en 1 hasta llegar
# a otro número primo que sea divisible entre "n" sin que haya residuo.
primo = 2

# Mientras "n" no sea 1 sigue dividiendo.
while n > 1:

    # Aquí revisa si el número "n" es divisible entre el número al que
    # corresponde la variable "primo" en la iteración que se encuentre. Esta
    # condicional no aumenta el contador de la variable "primo", porque es
    # posible que al dividirla entre un número primo, el resultado se pueda
    # dividir otra vez entre ese mismo primo. Ejemplo 81 es divisible entre 3,
    # da igual 9 que también es divisible entre 3.
    if n % primo == 0:

        # Si no hay residuo cuando se divide por este número se agrega a la
        # lista.
        factores_primos.append(primo)
        
        # Se divide entre el primo en la iteración en curso para encontrar
        # otro factor primo. Como se mencionó antes, puede que el "n"
        # resultante se pueda dividir entre el mismo "primo" de la iteración
        # actual.
        n = n/primo

    # Le aumenta 1 al contador "primo" cuando en la iteración actual, en "n"
    # que esté guardado en este momento ya no es divisible entre el "primo"
    # actual, hace esto hasta encontrar otro número (el cual será primo), que
    # pueda dividir el "n" gurdado en memoria hasta este momento sin dejar
    # residuo.
    else:
        primo += 1

# Imprime el último primo encontrado y guardado en la lista de factores
# primos, siempre será el mayor factor primo encontrado porque fuimos
# recorriendo los número más bajos a los más altos.
print(factores_primos[-1])