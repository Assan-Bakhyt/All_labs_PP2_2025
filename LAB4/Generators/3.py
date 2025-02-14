def mygenerator(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        
n = int(input("Enter: "))
g = mygenerator(n)

for x in g:
    print(x)