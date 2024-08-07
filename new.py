#number guessing game 
import random
correctNum = random.randint(1,10)

while True :
    Guess = int(input("Enter your guess from (1 - 10)  : "))
    if (Guess == correctNum) :
     print ("you guessed the right number : {correctNum} ")
     break
    elif Guess > correctNum:
         print("Guess a little bit smaller ")
    elif Guess < correctNum :
         print ("Guess a little bit higher")
    else :
         print ("please try again :( ")

print("congra")