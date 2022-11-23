def f(x, y=1):
    return x * y

# print(f(3))
#
# print(f(3, 4))

def g(x, y=2, z=3):
    return x * y + z

print(g(10))

print(g(10, 5))

print(g(10, z=20))

print(g(z=4, x=100))
