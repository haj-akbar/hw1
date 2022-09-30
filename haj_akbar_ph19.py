#The final speed of releasing the ball on the ground!!
from math import sqrt
height = float(input("Enter height : "))
#first speed = 0 in_radical + 0 = in_radical
in_radical = (2 * (9.8 * height))
final_speed = sqrt(in_radical)
print("final speed :" , final_speed)