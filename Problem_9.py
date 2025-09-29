def factorial(n):
    n_factorial = 1
    for i in range(1, n+1):
        n_factorial = n_factorial * i
    return n_factorial

def combinatoria (n, k):
    combinatoria = factorial(n) / (factorial(k) * factorial(n - k))
    return int(combinatoria)

a = combinatoria(9, 3)
a