# Goal was to create a simple program to calculate amount owed at a dinner. Needs to know total amout, tip percentage and number of guests.






def tip_calc():
  total_amount = input("what was the total bill amount ")
  tip_amount = input('what amount would you like to tip, 5, 10, 12, 15? ')
  guest_amount = input('How many guests will you be splitting between today? ')
  final_tip = float(tip_amount) / float(total_amount) * 100
 

  user_total = (float(total_amount) + float(final_tip)) / float(guest_amount)
  print(f'Your total is {round(user_total,2)}')

   
        




tip_calc() 