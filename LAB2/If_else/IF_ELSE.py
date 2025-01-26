#1 If

a = 33
b = 200
if b > a:
    print("b is greater than a")

#2 Elif

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#3 Else

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#4 Short Hand if
a = 200
b = 33

if a > b: print("a is greater than b")

#5
a = 2
b = 330
print("A") if a > b else print("B")

#6 And
a = 200
b = 33 
c = 550
if a > b and c > a:
    print("Both conditions are True")

#7 Or

a = 200
b = 33
c = 500
if a > b or c > a:
    print("At least one of the conditions is True")

#8 Not

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

#9 Nested if

x = 41

if x > 10:
    print("above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("But not above 20.")
#10 The pass Statement

a = 33
b = 200

if b > a:
    pass
