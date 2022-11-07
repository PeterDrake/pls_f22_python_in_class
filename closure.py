# def x(a):
#     def y(b):
#         return a + b
#     a = a + 1
#     return y
#
# z = x(2)
# print(z(3))

def counter():
    box = [0]
    def y():
        box[0] += 1
        return box[0]
    return y

c1 = counter()
c2 = counter()
print(c1())
print(c1())
print(c1())
print(c2())
print(c2())
print(c2())
