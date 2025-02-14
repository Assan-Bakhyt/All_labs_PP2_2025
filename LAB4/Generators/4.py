def squares(a,b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
g = squares(a,b)

for x in g:
    print(x)