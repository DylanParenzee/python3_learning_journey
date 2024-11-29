#Create and use list data structure
#Implement features to read a text file and write data to a text file
#Apply appropriate language syntax rules
#Develop code using data types, variables, and variable scope
#Create expressions in selection and iteration constructs using logical operators
#Develop appropriate algorithm using sequence, selection, and iteration constructs
#Use commenting features inside code to provide appropriate information about functions
#Write code to apply string manipulation features and any other mathematical formulae to implement required features
#Use program library functions

def sort(): #A function to sort through phases or words from the user input and convert to pig latin
  phrase = input('what is your phrase? ') # takes input from user and saves it to the variable "Phrase"
  split_phrase = phrase.split() # takes the phrase and splits it into a list with individual words
  for words in split_phrase : # loops through each word 
      if words[0] == "a":
        print(f"{words} - way ")
      else:
        print(words[1:] + words[0] + "ay ", end="")
    
  






sort()