def criba_eratostenes(n):
    primos = []
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False
    for i in range(2, n + 1):
        if es_primo[i]:
            primos.append(i)
            for j in range(i * i, n + 1, i):
                es_primo[j] = False
    return primos