name = "Vishal"
print(name[2])
print(name)

for i in name:
    print(i)

msg = "my name is vishal singh"
print(msg[1:10]) # here start point is one and end point is  10-1 = 9
# reverse
print(msg[3:10:2])
print(msg[10:0:-1]) # -1 ia jump point
# complete reversal
print(msg[::-1])
print(msg[-1]) # print form backward direction
print(msg[2:-6]) #forward directio pos move, neg is backward dirction

for i in msg:
    if(i=="s"):
        print("I got s as a sting: ")
    print(i)
