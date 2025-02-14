def mygenerator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

n = int(input("Enter: "))

g = mygenerator(n)

print(",".join(map(str, g)))