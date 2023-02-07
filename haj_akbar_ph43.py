#ATM(I say the name instead of the number)!!
bank_account =float(input("how much is your account balance ?  "))
bank_note_100000 = (bank_account // 500)
left_over = (bank_account % 500)
bank_note_50000 = (left_over // 100)
left_over = (left_over % 100)
bank_note_10000 = (left_over // 50)
left_over = (left_over % 50)
bank_note_5000 = (left_over // 10)
left_over = (left_over % 10)
bank_note_5 = (left_over // 5)
left_over = (left_over % 5)
bank_note = (left_over // 1)
print("cerashe abde" , bank_note_100000)
print("ebi mo tala" , bank_note_50000)
print("emonoel makroon" , bank_note_10000)
print("agha joorj washington" , bank_note_5000)
print("agha wiliam shakspier" ,bank_note_5 )
print("zibaye khofte monaliza" , bank_note)





