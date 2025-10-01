# Problem 4:
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit number is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


n = [9, 0, 0]
m = [9, 0, 0]

palindrome = []

for k in range(10):
    m[1] = k
    for l in range(10):
        m[2] = l
        for i in range(10):
            n[1] = i
            for j in range(10):
                n[2] = j

                N = int(str(n[0]) + str(n[1]) + str(n[2]))
                M = int(str(m[0]) + str(m[1]) + str(m[2]))

                R = N * M
                R_str = str(R)

                if R_str == R_str[::-1]:
                    palindrome.append(R)

print(max(palindrome))