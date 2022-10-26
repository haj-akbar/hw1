#idendtification!!
number_user = int(input("enter number of characters of your name : "))
if (number_user >= 3) and (number_user <= 10):
    user_name = input("enter your name : ")
    q_sum = len(user_name)
    if q_sum == number_user :
        print("true")
    else:
        print("eror")
else:
    print("eror")      