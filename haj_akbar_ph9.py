#"bank interst every year!"
Balance = float(input("Enter your account amount:"))
first_year = ((4 * Balance) / 100)
first_year = round(first_year,2)
print ("In the first year , you will receive",first_year,"euros interest")
first_year = (first_year + Balance)
second_year = ((4 * first_year ) / 100)
second_year = round(second_year,2)
print ("In the second year , you will receive",second_year,"euros interest")
second_year = (second_year + first_year)
third_year = ((4 * second_year) / 100)
third_year = round(third_year,2)
print ("In the third year , you will receive",third_year,"euros interest")



