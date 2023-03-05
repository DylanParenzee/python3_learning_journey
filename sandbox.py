

#20.03.23

#playing around with variables 

num_of_cats = 10 

print(num_of_cats * 2)

# as part of colt steel's python course test 

# 24.02.23
# Define a variable named city and set it equal to any string
city = "Sydney"

# Define a variable named price and set it equal to any float
price = 23.99

# Define a variable named high_score and set it equal to any int
high_score = 2983729

# Define a variable named is_having_fun and set it to a Boolean value
is_having_fun = True


# 25.02.23

 # Set the message variable equal to any string containing a new-line escape sequence
message = "hello there \n how are you"


# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!
mountains = "/\\/\\/\\"


# Set the quotation variable to any string that contains an escaped double quotation mark

quotation = "\"time\""


#String Concatenation Exercise
#Set the variable called greeting  to some greeting, e.g. "hello".

#Set the variable called name  to some name, e.g. "Heisenberg".

#Then set the variable called greet_name  so that it concatenates greeting , name , and a space " " between them.

greeting = "Hello there"
name = "Anikin Skywalker"
greet_name = greeting + " " + name



#26.02.23

#Formatting Strings
#Set the variable called first  to your first name.

#Set the variable called last  to your last name.

#Then set the variable called formatted  that interpolates both using the .format()  method.  Make sure you follow this pattern:

first = "John"
last = "Doe"

formatted = "First Name: {}, Last Name: {}".format(first, last)


#04.02.23

name = 'john snow'

if name == "arya stark" :
    print('valar morghulis')
elif name == 'john snow':
    print('you know nothing')
else:
     print('Carry on')        


from random import randint
choice = randint(1,10)



if choice == 7:
    print('lucky')
else:
    print('unlucky sorr try again ')
