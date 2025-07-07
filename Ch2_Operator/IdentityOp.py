# indentity operator 
# is and is not
# compare object
a = 5
b = 5
print(a is b)
# In python memory managents reuse the obect, istead of creating new object for the same data and same datatype
print(a==b) # it is differnts than is operator
print(id(a))
print(id(b))
print(a is not b)
# is return ture only when memeory address is same.
x = 10
y = 10
print(id(x))
print(id(y))
print(x is b)

p =5
print(id(p))
p =6
print(id(p))