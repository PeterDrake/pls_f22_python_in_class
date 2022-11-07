class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

v = Vector(2, 3)

w = Vector(1, 4)

x = v

v += w

print(x)
