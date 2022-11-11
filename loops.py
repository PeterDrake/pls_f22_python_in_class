x = 0
while True:
    print(x)
    x += 1
    if x >= 3:
        break


sum = 0
for i in range(1000):
    sum += i
print(sum)


def numbers():
    x = 0
    while True:
        x += 1
        yield x

for i in numbers():
    print(i)
    if i >= 10:
        break

#print([x for x in numbers() if x < 10])

