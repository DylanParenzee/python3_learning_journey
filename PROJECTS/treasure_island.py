#This file will include the Treasue Island interactive game project and the learnings for it. 


#conditinal logic and flow control 

#exercise

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif (bmi > 18.5 ) and (bmi< 25):
    print('normal weight')
else: 
    print('overweight')


#game 

def start_game():
   want_to_play = input("Helo would you like to play a game    y or n ? ")
   if want_to_play == "y":
      print("Awesome, Lets play treasure island!")
      game_logic()
   else:
    print("No problem, have a good day!")






def game_logic():
  return none 