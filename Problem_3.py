# Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

factores_primos = []
n = 600851475143
i = 2
while n > 1:
    if n % i == 0:
        factores_primos.append(i)
        n = n/i
    else:
        i += 1
print(max(factores_primos))