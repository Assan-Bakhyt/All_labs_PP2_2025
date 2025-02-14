def generator(n):
    for i in range(n,-1,-1):
        yield i

n = int(input("Enter: "))
g = generator(n)

for x in g:
    print(x)