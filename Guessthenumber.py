# # GAME to Guess a random integer between the Given Range....

import random
n=random.randint(1,100)

#Guess the integer :
while True : 
    user_guess=(input("Guess a number between (1,100) OR Press (Q) to Quit : "))
    if(user_guess=="Q"):
        print("--GameOver--")
        print("User Left The Game")
        break
    user_guess=int(user_guess)
    
    if(user_guess==n):
        print("Success:Your guess is Correct!!!")
        print("---GameOver---")
    elif(user_guess<n):
        print("Enter Larger Integer")
    else:
        print("Enter Smaller Integer")











