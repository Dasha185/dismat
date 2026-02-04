def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def combinations(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def permutation(n, repetitions):
    result = factorial(n)
    for rep in repetitions:
        result //= factorial(rep)
    return result

print("1.1:", permutation(7, []))
print("1.2:", permutation(7, [2]))
print("1.3:", permutation(8, [2, 2, 2]))
print("1.4:", combinations(12, 3) * combinations(5, 2))
print("1.5:", permutation(10, [2, 3, 3, 2]))
print("1.6:", 5 * 4)