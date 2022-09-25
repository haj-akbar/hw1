#"calculation of the amount of profit and food"
price_meal = float(input("please enter the price of your meal:"))
Tax = ((9 * 100) / price_meal)
Tip = ((18 * 100) / price_meal)
Sum = (Tax + Tip + price_meal)
Total = round(Sum , 2)
print("you must pay",Total,"pound")
