def tripleta_ordenada(n):
    l = []
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                suma = i + j + k
                pitagoras = i**2 + j**2
                orden = i < j < k
                if suma == 1000:
                    l.append([i, j, k])
    return l


a=tripleta_ordenada(1000)
print(a)