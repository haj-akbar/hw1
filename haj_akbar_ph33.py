#A bakers dream !!
number_fr = int(input("would you like fresh bread : "))
number_yest = int(input("would you like yesterday bread : "))
price_fresh_bread = (3.69 * number_fr)
price_yesterday_bread = (((3.69 * 40) / 100) * number_yest)
total = (price_fresh_bread + price_yesterday_bread)
print("total : " , total )