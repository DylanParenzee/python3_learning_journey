# Goal was to create a simple program to calculate amount owed at a dinner. Needs to know total amout, tip percentage and number of guests.






def tip_calc():
  total_amount = input("what was the total bill amount ")
  tip_amount = input('what amount would you like to tip, 5, 10, 12, 15? ')
  guest_amount = input('How many guests will you be splitting between today? ')
  final_tip = int(tip_amount) / int(total_amount) * 100
 

  user_total = (int(total_amount) + int(final_tip)) / int(guest_amount)
  print(f'Your total is {user_total} ')

   
        




tip_calc() 