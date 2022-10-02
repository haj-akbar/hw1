#Calculate the area of the triangle(again)!!
from math import sqrt
side_1 = float(input("enter the side1 : "))
side_2 = float(input("enter the side2 : "))
side_3 = float(input("enter the side3 : "))
s = ((side_1 + side_2 + side_3) / 2)
area = sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
print("The area is equal to " , area)