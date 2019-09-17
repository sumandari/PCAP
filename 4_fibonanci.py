def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

# test
for n in range(1, 10):
    print(n, "->", fib(n))

# dengan recursion
def fib2(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib2(n - 1) + fib2(n - 2)

# test
for n in range(1, 10):
    print(n, "->", fib2(n))
