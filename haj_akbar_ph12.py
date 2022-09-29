#calculation distance between two geographic points
from math import radians , cos , sin , acos 
lat1 = float(input("enter latitude1 :"))
long1 = float(input("enter longitude1 :"))
lat2 = float(input("enter latitude2 :"))
long2 = float(input("enter longitude2 :"))
lat1 =radians(lat1)
long1 =radians(long1)
lat2 =radians(lat2)
long2 =radians(long2)
distance = 3963 * acos((sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(long2 - long1))
convert_to_kilo_meters = (distance * 1.609344)
print("The distance between two geographical points is equal to" , convert_to_kilo_meters)
