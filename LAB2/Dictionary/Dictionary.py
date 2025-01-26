#1

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

#2

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

#3

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red","white","blue"]
}
print(thisdict)

#4

thisdict = dict(name = "John", age = 36,country = "Norway")
print(thisdict)

#5

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "Year": 1964
}
x = thisdict["model"]
x2 = thisdict.get("model")
x3 = thisdict.keys()
print(x)
print(x2)
print(x3)

#6
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) # before the change
car["color"] = "white"
print(x) # after the change

#7
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)

#8
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#9
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#10
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(x)

#11
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#12
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#13
thisdict = {
    "brand": "Ford",
    "model": "Mustange",
    "year": 1964
}
if "model" in thisdict:
    print("Yes,'model' is one of the keys in the dictionary")

#14
thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#15
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "Year": 1964
}
thisdict.update({"Year":2020})
print(thisdict)
#16
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#17
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
#18
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#19
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#20
thisdict = {
     "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

#21
thisdict = {
     "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

#22

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)

#23

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(thisdict[x])

#24

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
    print(x)
for x in thisdict.keys():
    print(x)
for x,y in thisdict.items():
    print(x,y)

#25

thisdict = {
     "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#26

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#27
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#28

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

#29
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

#30

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
