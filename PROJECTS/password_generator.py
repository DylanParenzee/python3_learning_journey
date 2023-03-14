# goal is to generate a random 10 character password utilising upper and lowercase charcter, symbols and numbers. 

import random 

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = "!@#$%^&*()_+?./\]"
numbers = '0123456789'




print(f'Your Passoword is :')
for i in range(1,13):
    print(random.choice(lower_case + upper_case + symbols + numbers), end="")