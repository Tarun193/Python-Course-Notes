# "Guess the number" 
# in  we genrate a random number between 0-100 or you can chose your range according to your choice. Then we ask user to guess the number , then we throw hints by suggesting that if user guessed number is less or more than the radom number. Then we ask user to again guess the number , we again give hints and to these again and again untill the number becomes equal to randomly genrated number.Atlast we return number of guesses user to took to guess the number.


import random



random_number = random.randint(0,100)
number = int(input("Guess the number(0-100):"))
guesses = 1

while number != random_number and guesses <= 5:
    if number < random_number:
        print("Number is too low!!")
    if number > random_number:
        print("Number is too high!")
    number = int(input("Guess the number(0-100):"))
    guesses += 1

if guesses > 5:
    print("You lost the game!!!")
else:
    print("you took ",guesses," Number of guesses")