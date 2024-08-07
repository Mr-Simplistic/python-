#number guessing game 
import random
correctNum = random.randint(1,10)

Guess = int(input("Enter your guess from (1 - 10)  : "))
while Guess != correctNum :
    Guess = int(input("Enter your guess from (1 - 10)  : "))
    if (Guess == correctNum) :
     print ("you guessed the right number : 7 ")
    elif Guess > correctNum:
         print("Guess a little bit smaller ")
    elif Guess < correctNum :
         print ("Guess a little bit higher")
    else :
         print ("please try again :( ")
