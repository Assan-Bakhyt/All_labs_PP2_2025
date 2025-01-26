#1

thistuple = ("apple","banana","cherry")
print(thistuple)

#2

thistuple = ("apple","banana","cherry","apple","cherry")
print(thistuple)

#3

thistuple = ("apple","banana","cherry")
print(len(thistuple))

#4

thistuple = ("apple",)
print(type(thistuple))

#Not a tuple
thistuple = ("apple")
print(type(thistuple))

#5

tuple1 = ("apple","banana","cherry")
tuple2 = (1,5,7,9,3)
tuple3 = (True,False,True)

print(tuple1)
print(tuple2)
print(tuple3)

#5
tuple1 = ("abc",34,True,40,"Male")
print(tuple1)

#6 

thistuple = tuple(("apple","banana","cherry"))
print(thistuple)
"""
    Список - это коллекция, которая упорядочена и может быть изменена. Позволяет создавать дубликаты элементов.
    Кортеж - это коллекция, которая упорядочена и не подлежит изменению. Позволяет создавать дубликаты элементов.
    Набор – это коллекция, которая не упорядочена, неизменяемый* и неиндексированный. Никаких дубликатов участников.
    Словарь – это коллекция, которую упорядочивают** и изменчивые. Никаких дубликатов участников.
"""

#7

thistuple = ("apple","banana","cherry")
print(thistuple[1])

#8

thistuple = ("apple","banana","cherry")
print(thistuple[-1])

#9

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#10

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[:4])

#11

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:])

#12

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#13

thistuple = ("apple","banana","cherry")
if "apple" in thistuple:
    print("Yes,'apple' is in the fruits tuple")

#14

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#15

thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#16

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#17

thistuple = ("apple" , "banana" , "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#18

"""thistuple = ("apple","banana","cherry")
del thistuple
print(thistuple)"""  #this will raise an error because the tuple no longer exists

#19

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry","trawberry","raspberry")

(green,yellow,*red) = fruits

print(green)
print(yellow)
print(red)

#20

fruits = ("apple","mango","papaya","pnieapple","cherry")

(green,*tropic,red) = fruits

print(green)
print(tropic)
print(red)

#21

thistuple = ("apple","banana","cherry")
for x in thistuple:
    print(x)

#22

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#23

thistuple = ("apple","banana","cherry")
i = 0
while i < len(thistuple):
   print(thistuple[i])
   i = i + 1
#24

tuple1 = ("a","b","c")
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)

#25

fruits = ("apple","banana","cherry")
mytuple = fruits * 2

print(mytuple)

#26

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

#27

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)