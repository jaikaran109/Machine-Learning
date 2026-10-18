# Permutation and Combination Program
# Permutation: nPr = n! / (n - r)!
# Combination: nCr = n! / [r! * (n - r)!]


def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


n = int(input())
r = int(input())

if r > n or n < 0 or r < 0:
    print("Invalid Input")
else:
    permutation = factorial(n) // factorial(n - r)
    combination = factorial(n) // (factorial(r) * factorial(n - r))
    print("Permutation (nPr): " + str(permutation))
    print("Combination (nCr): " + str(combination))
