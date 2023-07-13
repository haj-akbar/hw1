#richter scale!!!
magnitude = float(input("enter rechter number : "))
if magnitude < 2 :
    print("micro")
if (magnitude < 3) and (magnitude >= 2) :
    print("very minor")    
if (magnitude < 4) and (magnitude >= 3) :
    print("minor")       
if (magnitude < 5) and (magnitude >= 4) :
    print("light")       
if (magnitude < 6) and (magnitude >= 5) :
    print("moderale")       
if (magnitude < 7) and (magnitude >= 6) :
    print("strong")       
if (magnitude < 8) and (magnitude >= 7) :
    print("major")       
if (magnitude <= 10) and (magnitude >= 8) :
    print("great")       
if  (magnitude > 10) :
    print("meteoric")       
