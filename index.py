str=input("enter the string %d")
print(str)
i=input("enter the i value ")
i=int(i)
if len(str) == 0:
    print("Empty string")

elif i <  len(str):
    print(str[i])
else:
    print("i is out of range")
