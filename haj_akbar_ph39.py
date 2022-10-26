#noise measurement!!
noise_room = float(input("enter noise of the rooom : "))
if noise_room >= 130 :
    print("wtf!!")
elif (noise_room >= 106) and (noise_room < 130):
    print("what do you do ?!")
elif (noise_room >= 70) and (noise_room < 106):
    print("not bad")
else:
    print("nice room")            