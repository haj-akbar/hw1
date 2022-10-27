#deteirmine month!!
month = input("enter the month : ")
if (month == "farvardin") or (month == "ordibehesht") or (month == "khordad") or (month == "tir") or (month == "mordad") or (month == "shahrivar"):
    print("31")
elif (month == "esfand"):
    print("29")
else:
    print("30")        
#اگر کاربر اشتباه تایئ کند یا اصلا ناهی را ننویسد باز بهش 30 نمایش داده می شود!!    