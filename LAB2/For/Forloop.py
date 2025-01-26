#1 Python For Loops

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

#2 Looping Through a String

for x in "banana":
  print(x) 

#3 The break Statement

fruits = ["apple","banana","cherry"]
for x in fruits:
   print(x)
   if x == "banana":
      break
#4 The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#5 the range() Function

for x in range(6):
   print(x)

#6 The pass Statement
for x in [0,1,2]:
   pass