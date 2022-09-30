#calculate the volume of the cylinder!!
from math import pi
radius = float(input("Enter radius : "))
height = float(input("Enter height : "))
area_circle = ((radius ** 2) * pi)
volume = round(( area_circle * height) , 1 )
print("volume of the cylinder" , volume)