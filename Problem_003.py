# Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

factores_primos = []
n = 600851475143

# Primer número primo, después comenzará a sumar de 1 en 1 hasta llegar
# a otro número primo que sea divisible entre n sin que haya residuo.
primo = 2

# Mientras n no sea 1 sigue dividiendo.
while n > 1:

    # Si no hay residuo cuando se divide por este número, se agrega a la lista
    # y se divide entre el primo en la iteración en curso para encontrar otro
    # factor primo.
    if n % primo == 0:
        factores_primos.append(primo)
        n = n/primo

    # Si hay residuo, suma 1 al contador de los números primos, hasta llegar a
    # otro, lo encuentra porque ya se dividio entre el primo más pequeño sin
    # residuo, como solo dividirá entre números primos y no números compuestos
    # como 4, 9, 10.
    else:
        primo += 1
print(max(factores_primos))