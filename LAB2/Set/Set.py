#1

myset = {"apple","banana","cherry"}
print(myset)

#2

thisset = {"apple","banana","cherry","apple"}
print(thisset)

#3

thisset = {"apple","banana","cherry",True,1,2}
print(thisset)

#4

thisset = {"apple","banana","cherry"}
print(len(thisset))

#5

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1,set2,set3)

#6

set1 = {"abc", 34, True, 40, "male"}
print(set1)

#7

myset = {"apple","banana","cherry"}
print(type(myset))

#8

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#9

thisset = {"apple","banana","cherry"}
for x in thisset:
    print(x)

#10

thisset = {"apple","banana","cherry"}
print("banana" not in thisset)

#11

thisset = {"apple","banana","cherry"}

thisset.add("orange")

print(thisset)

#12

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#13

thisset = {"apple","banana","cherry"}
mylist = ["kiwi","orange"]

thisset.update(mylist)

print(thisset)

#14

thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

#15

thisset = {"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

#16

thisset = {"apple","banana","cherry"}
x = thisset.pop()
print(x)
print(thisset)

#17

thisset = {"apple","banana","cherry"}
thisset.clear()
print(thisset)

#18

"""thisset = {"apple","banana","cherry"}
del thisset
print(thisset)"""  #this will raise an error because the set no longer exists

#19

thisset = {"apple","banana","cherry"}

for x in thisset:
    print(x)

#20

set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

#21

set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1 | set2
print(set3)

#22

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2,set3,set4)
print(myset)

#23

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"John","Elena"}
set4 = {"apple","bananas","cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

#24

x = {"a","b","c"}
y = (1,2,3)

z = x.union(y)
print(z)

#25

x = {"a","b","c"}
y = {1,2,3}

x.update(y)
print(x)

#26

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1.intersection(set2)
print(set3)

#27

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1 & set2
print(set3)

#28

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set1.intersection_update(set2)
print(set1)

#29

set1 = {"apple",1,"banana",0,"cherry"}
set2 = {False,"google",1,"apple",2,True}

set3 = set1.intersection(set2)

print(set3)

#30

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

#31

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1 - set2
print(set3)

#32

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set1.difference_update(set2)
print(set1)

#33
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

#34

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1 ^ set2

print(set3)