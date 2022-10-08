#Convert seconds to days,hours and minutes!!
seconds = float(input("enter the seconds : "))
days = (seconds // 86400)
left_over = (seconds % 86400)
hours = (left_over // 3600)
left_over = (seconds % 3600)
minutes = (left_over // 60)
left_over = (seconds % 60)
print(days , ":" , hours , ":" , minutes , ":" , left_over)