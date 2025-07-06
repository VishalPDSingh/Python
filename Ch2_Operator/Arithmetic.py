# Operator In Python
# Arithmetic Operator
# Comparisson Operator 
# Logical Operator
# Bitwise Operator 
# Assignment Operator
# Identiy
# MemberShip 

# Aritmatic operator
a = 10
b = 15
print("Sum is ",(a+b))
print("Sub is ",(a-b))
print("Mul is ",(a*b))
print("div is ",(a/b)) # divsion always gives the floating number, if we want witho floating value then use floor divison(//)
print("mod is ",(a%b))
print("Floor Division is ",(a//b)) # it give int value 
print("Power is ",a**b)
# in the expression pecedence of operataor is
# first (), secnond **, third *,/, //, % from left to right, fourth +,-
print(5+2*3-1+10/5)


# Task 
# Caluclate_BMI, Formula is: weight/height
weight = int(input("Enter the weight of your body: "))
height = int(input("Enter the height of your body: "))
BMI = weight/height
print("Body mass index is: ",BMI)
print(type(BMI))