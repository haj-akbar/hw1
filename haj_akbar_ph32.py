#sort the numbers!!
the_first_number = float(input("Enter first numbers : "))
the_second_number = float(input("Enter second numbers : "))
the_third_number = float(input("Enter third numbers : "))
sum = ( the_first_number + the_second_number + the_third_number )
maxim = (max(the_first_number , the_second_number , the_third_number))
minim = (min(the_first_number , the_second_number , the_third_number))
center = (sum - (maxim + minim))
print("max : " , maxim , "center : " , center , "min : " , minim)