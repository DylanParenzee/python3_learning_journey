#This file will include the Treasue Island interactive game project and the learnings for it. 


#conditinal logic and flow control

first_choice = input('you are at a cross road, left or right\n').lower()

def red():
   print("A ROOM FULL OF FIRE, GAME OVER")

def blue():
   print('AN ANGRY TROUT ATTACKS YOU, GAME OVER')

if first_choice == 'left':
    print("A good choice... who knows what would have happened had you gone left...")
    second_choice = input("You can see the island, will you swim or wait for the boat? \n type 'swim' or 'wait'\n ").lower()
    if second_choice == 'wait':
      third_choice = input('Your boat has arrived and taken you to the island where there are three doors \n Red \n Blue \n Yellow \n Which do you choose?\n Type "red", "blue" or "yellow"\n ').lower()
      if third_choice == 'yellow':
         print('You Win!')
      elif third_choice == "red":
         red()
      elif third_choice == 'blue':
         blue()
    else:
       print('SHARK INFESTED WATER, GAME OVER')
else:
    print('Game Over')


