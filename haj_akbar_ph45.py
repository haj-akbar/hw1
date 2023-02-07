#Black or white chess houses!!
letter  = input("Enter the letter you want : ")
number = int(input("Enter the number you want : "))
if (number % 2) == 0 :
     x = 1
else:
     x = 0 
#1 = even
if (letter == "a") or (letter == "c") or (letter == "e") or (letter == "g"):
    if x == 1 :
        print("white")
    else:
        print("black")
else:
    if x == 1 :
        print("black")
    else:
        print("white")   
    