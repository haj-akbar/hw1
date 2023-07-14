#season from month and day!!!
season = input("enter month : ")
day = int(input("enter day : "))
if (season == "march")  or (season == "april")  or (season == "may") or (season == "june"):
    if (day < 20 ) and (season == "march"):
        print("winter")
        exit(0)
    if (season ==  "june") and ( day < 21):
         print("summer")
         exit(0)
    print("spring")
if (season ==  "july") or (season ==  "agust") or (season ==  "september"):
    if (season ==  "september") and (day > 22):
        print("fall")
        exit(0)
    print("summer")
if (season ==  "october") or (season ==  "novamber") or (season ==  "december"):
    if (season ==  "december") and (day > 21) : 
        print("witer")
        exit(0)
    print("fall")
if (season ==  "january") or (season ==  "february"):
    print("winter")
