#ATM !!
bank_account =float(input("how much is your account balance ? = "))
bank_note_100000 = (bank_account // 100000)
left_over = (bank_account % 100000)
bank_note_50000 = (left_over // 50000)
left_over = (left_over % 50000)
bank_note_10000 = (left_over // 10000)
left_over = (left_over % 10000)
bank_note_5000 = (left_over // 5000)
left_over = (left_over % 5000)
bank_note_2000 = (left_over // 2000)
left_over = (left_over % 2000)
bank_note_1000 = (left_over // 1000)
left_over = (left_over % 1000)
bank_note_500 = (left_over // 500)
print("bank_note_100000" , bank_note_100000)
print("bank_note_50000" , bank_note_50000)
print("bank_note_10000" , bank_note_10000)
print("bank_note_5000" , bank_note_5000)
print("bank_note_2000" , bank_note_2000)
print("bank_note_1000" , bank_note_1000)
print("bank_note_500" , bank_note_500)






