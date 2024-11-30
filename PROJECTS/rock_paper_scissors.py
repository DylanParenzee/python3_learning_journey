# create a rock paper scissors guessing game for 2 players from terminal
 
 
 


def get_inputs():
   player_1_input = input(f"player 1's' choice is ")
   player_2_input = input(f"player 2's choice is ")
   if player_1_input == "rock" and player_2_input == "paper":
    print("Winner = Player 2! Paper beats rock")
   elif player_1_input == "rock" and player_2_input == 'scissors':
    print(f'Winner = Player 1! rock beats scissors')
   elif player_1_input == "scissors" and player_2_input == 'rock':
    print(f'Winner = Player 2! rock beats scissors')
   elif player_1_input == "scissors" and player_2_input == 'paper':
    print(f'Winner = Player 1! scissors beats paper')
   elif player_1_input == "paper" and player_2_input == 'rock':
    print(f'Winner = Player 1! paper beats rock')
   elif player_1_input == "paper" and player_2_input == 'scissors':
    print(f'Winner = Player 2! scissors beats paper')
   else: print(f'its a draw!')

game_continue = input('continue game ? y or n ')


get_inputs()