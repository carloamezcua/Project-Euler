def factores_primos(n):
    factores = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factores