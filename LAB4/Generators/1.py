# 1 method 
a = int(input("Enter: "))

g = (x**2 for x in range(a))
print(list(g))

# 2 method
def mygenerator(n):
    for x in range(n):
        yield x**2

n = int(input("Enter: "))

g2 = mygenerator(n)
for i in g2:
    print(i, end=" ")
