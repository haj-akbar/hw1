#triangle type detection!!
first_edge = float(input("enter first edge : "))
second_edge = float(input("enter second edge : "))
third_edge = float(input("enter third edge : "))
if (first_edge == second_edge) and (second_edge == third_edge):
    print("motesavy olazla")
elif(first_edge == second_edge) or (second_edge == third_edge) or (first_edge == third_edge):
    print("motesavy olsaghayn")
else:
    print("mokhtalefolazla")        