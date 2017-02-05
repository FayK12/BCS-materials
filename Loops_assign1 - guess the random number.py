from random import randint
num = randint(1,100) #the number for user to guess, randomly generated

print("I'm thinking of a number between 1-100. You have 7 guesses.")
guess = 1 #guess counter, keeps track of how many guesses have been mae
random = int(input("Guess 1: "))  #tracks user guesses

while ((random != num) and (guess < 7)):
    if (random) > num:
        print("Too high")
        guess = guess + 1 
        random = int(input("Guess " + str(guess) + ": "))
        
    elif (random) < num:
        print("Too low")
        guess = guess + 1 
        random = int(input("Guess " + str(guess) + ": "))
    

if (guess ==7) and (random != num):
    print("You're a horrible mind reader. I was thinking of " + str(num)) 

if (random == num):
    print ("You made that look too easy... it took you " + str(guess) + " guess(es)")

