#MAKING A ROCK PAPER SCISSORS APPP
#TIYIN O 22/02/2025

import random

outcomes = {1: "Rock",
            2 : "Paper",
            3 : "Scissors"}

players = {1 : "You",
           2 : "Robot"}

user_id = 1
bot_id = 2

'''
count = 0
while count <= 20 :
   print("Robot Choice: ", outcomes[bot_choice])
   count+= 1

   '''

bot_choice  = random.randint(1, 3)

print()

while True:
    user = input("Enter Rock, Paper Scissors: ")

    if user == "rock" :
       print("Your Choice is: ", outcomes[1])
       user = 1
       break

    elif user == "paper" :
        print("Your Choice is: ", outcomes[2])
        user = 2
        break

    elif user == "scissors" :
        print("Your Choice is: ", outcomes[3])
        user = 3
        break

    elif user == "quit" :
        break

    else :
        print("[!]ERROR: INVALID INPUT")


def choice_comparison(user, bot) :
    if user == bot :
        print("A TIE!")

    ##HUMAN WINNIJNG SCENARIO
    elif user == 1 and bot == 3 :
        print("YOU WIN!")
        return user_id
    
    elif user == 2 and bot == 1 :
        print("YOU WIN!")
        return user_id
    
    elif user == 3 and bot == 2:
        print("YOU WIN!")
        return user_id
    
    ##ROBOT WINNIJNG SCENARIO

    elif bot == 1 and user == 3 :
        print("ROBOT WINS!")
        return bot_id
    
    elif bot == 2 and user == 1 :
        print("ROBOT WINS!")
        return bot_id
    
    elif bot == 3 and user == 2:
        print("ROBOT WINS!")
        return bot_id

    else :
        print("A TIE") 


print("Bot Choice: " , outcomes[bot_choice])
print()

choice_comparison(user, bot_choice)
