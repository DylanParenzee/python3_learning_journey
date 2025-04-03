#little pizza delivery exercise from angela yu's 100 days of code

small_pizza = 15
medium_pizza = 20
large_pizza = 25
add_peperoni_small = 2 
add_peperoni_ml = 3 
extra_cheese = 1 

cost = 0 

user_selection = input("Welcome to Python Pizza Deliveries!\n" "What size Pizza would you Like?  S, M, or L ?  ").capitalize()
 
if user_selection == "S":
    cost += small_pizza
elif user_selection == 'M':
    cost += medium_pizza
elif user_selection == "L":
    cost += large_pizza



pepperoni = input("would you like peperoni on your pizza?  ").capitalize()

if pepperoni == 'Y' and user_selection == 'S':
    cost += add_peperoni_small
elif pepperoni == 'Y' and user_selection == 'M':
    cost += add_peperoni_ml
elif pepperoni == 'Y' and user_selection == 'L':
    cost += add_peperoni_ml
else:
    print('No pepperoni, got it! ')

cheese = input('Would you like extra cheese today for a cost of $1? Y or N  ').capitalize()

if cheese == "Y":
    cost += extra_cheese
print('No extra cheese, got it!')


    
print(f" The price of your pizza today is {cost} ")


