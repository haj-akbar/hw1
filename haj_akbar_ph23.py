#Calculate the area of poygons!!
from math import tan , pi
number_of_sides = int(input("enter the number of sides : "))
sum_of_sides = float(input("enter the sum of sides : "))
sum_of_sides = (sum_of_sides / 2)
area = (((sum_of_sides ** 2) * number_of_sides) / (4 * tan(pi / number_of_sides)))
print(" The area is equal to " , area)
