#conversion of units,first part :mile/gallons = ? liter/100kilometers!! 
select_unit = int(input("{convert 1.miles per gallons to liter per 100 kilometers} or 2.{liter per 100 kilometers to miles per gallons}: "))
if select_unit == 1 :
    miles_per_gallons = float(input("how many miles per gallons:"))
    liter_per_100_kilo_meters = (miles_per_gallons * 235.215)
    print(miles_per_gallons , "miles per gallons is equal to " , liter_per_100_kilo_meters , "liter per 100 kilometers")
elif select_unit == 2 :
    liter_per_100_kilo_meters = float(input("how many liter per 100 kilometers:"))
    miles_per_gallons = (liter_per_100_kilo_meters * 0.00425142954)
    print( liter_per_100_kilo_meters ,"liter per 100 kilometers is equal to" , miles_per_gallons , "miles per gallons" )     
else :
    print("you should insert 1 or 2!")
        
