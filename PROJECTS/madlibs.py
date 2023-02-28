#small madlibs project by kylie ying to practice string concatenation


# A couple ways to concat -- gonna go with the f string -- much easier and more what im used to.

#youtuber = "Dylan"

#print('please subsribe to ' + youtuber)
#print('please subsribe to {}'.format(youtuber))
#print(f'please subsribe to {youtuber}')


adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("Your favourite famous person: ")

madlib = f"computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}, what a good role model!"


print(madlib)