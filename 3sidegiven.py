import math
a=int(input("enther the fist lenght:"))
b=int(input("enther the second lenght:"))
c=int(input("enther the third lenght:"))
s=a+b+c/2
area=math.sqrt(s*s-a*s-b*s-c)
print("the area of the traingle:",area)