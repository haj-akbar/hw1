#"calculation of the amount of profit and food"
price_meal = float(input("please enter the price of your meal:"))
Tax = ((9 * price_meal) / 100)
Tip = ((18 * price_meal) / 100)
Sum = (Tax + Tip + price_meal)
Total = round(Sum , 2)
print("you must pay",Total,"pound")
