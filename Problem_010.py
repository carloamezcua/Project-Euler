# n = 10
# primos = [2]
# k = 3
# #while primos[-1] < n:
# for i in range(1, n):
#     if primos[-1] % k == 0:
#         k += 1
#         break
#     else:
#         primos.append(k)
#         k += 1
# print(primos, k)


n = 97
i = 2

while i <= n**(1/2):
    if n == 1:
        print(str(n) + " no es un número primo.")
        break
    if n % i == 0:
        print(str(n) +" es divisible entre " + str(i))
        print(str(n) + " no es primo.")
        break
    if n % i != 0:
        print(str(n) +" no es divisible entre " + str(i))
        i += 1
    if i > n**(1/2):
        print ("Es primo.")