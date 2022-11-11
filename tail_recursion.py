def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


def countdown(n):
    while True:
        if n == 0:
            return
        print(n)
        n -= 1


# countdown(10)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact(n, product=1):
    if n == 1:
        return product
    return fact(n - 1, n * product)


def fact(n):
    product = 1
    while True:
        if n == 1:
            return product
        product *= n
        n -= 1


print(fact(5))
