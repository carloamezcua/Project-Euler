def numeros_divisibles(n):
    divisibles = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisibles.append(i)
            divisibles.append(int(n / i))
    return sorted(divisibles)