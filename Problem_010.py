n = 3
i = 2

# Estas condicionales se agregaron porque el ciclo de abajo no funciona cuando
# n = 1,2 o 3.
if n == 1:
    print(" 1 no es primo.")
elif n == 2:
    print("2 es primo.")
elif n == 3:
    print("3 es primo")

# Esta parte solo funciona cuando n > 3. Es por eso que agregué los
# condicionales arriba.
while i <= n**(1/2):
    if n % i == 0:
        print(str(n) + " no es primo.")
        break
    if n % i != 0:
        i += 1
    if i > n**(1/2):
        print (str(n) + " es primo.")