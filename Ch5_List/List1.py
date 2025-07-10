l =["Vishal",345,56.8,"dfdgf"]
print(l)
print(l[0])
print(type(l))
print(type(l[1]))

#Empty list
l1 = []
print(type(l1))
l1 = "Visg"
print(l1)

#list can hold any type of value
l2 = ["vishal",True,79.6,67,45+56j]
for i in l2:
    print(type(i))
print(l2)

# print int value only
l3 = ["vishal",23,56,4,6.6,67,56.9,["jis",56,7.8,78],56+67j]
for i in l3:
    if type(i) == list:
        for j in i:
            print(type(j))
    if type(i) == int:
        print(i)
print(l3[0:5]) # This is also metho to print
print(l3[6:3]) # it give the blank 

lis = list(range(10))
print(lis)
