#Determining the type of bomb with its frequency!!
frequency = float(input("Enter your desired frequency : "))
if frequency == 261.63 :
    print("C4")
elif frequency == 293.66 :
    print("D4")
elif frequency == 329.63 :
    print("E4")
elif frequency == 349.23 :
    print("F4")
elif frequency == 392 :
    print("G4")
elif frequency == 440 :
    print("A4")
elif frequency == 493.88 :
    print("B4")
else :
    print("Undefined")