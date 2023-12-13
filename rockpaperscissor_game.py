'''
7 (Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws. Here are sample runs:
'''

import random

def rockpaperscissor(input):
    if input == 0:
        return "scissor"
    if input == 1:
        return "rock"
    if input == 2:
        return "paper"



computer = random.randint(0,3)
user = eval(input("Enter 0,1 or 2"))
chosen_value_comp = rockpaperscissor(computer)
chosen_value_user = rockpaperscissor(user)

if computer == user:
       print("The computer is " + chosen_value_comp + ". You are " +chosen_value_user+" too. Its a draw")
elif computer > user:
      print("The computer is " + chosen_value_comp + ". You are " +chosen_value_user + "Computer win")
elif user > computer:
    print("The computer is " + chosen_value_comp + ". You are " + chosen_value_user + " You win")