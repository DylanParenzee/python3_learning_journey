import random 



def guess():
    x = int(input('whats the max number to play to?'))
    rand_num = random.randint(1, x)
    guess = 0 
    while(guess != rand_num) :
        guess = int(input(f"Lets play a guessing game, guess a number between 1 and {x} "))
        if guess < rand_num:
            print('whoops too low, guess again')
        elif guess > rand_num:
            print('ohhh too high! guess again')
    print(f'You got it! good guess, the number was {rand_num}')
            


guess()