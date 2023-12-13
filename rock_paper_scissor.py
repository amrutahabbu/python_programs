import random
def rockpaperscissor(input):
    if input == 0:
        return "scissor"
    if input == 1:
        return "rock"
    if input == 2:
        return "paper"

win_continuos = 0
win_draw = 0
win_user = 0
win_comp = 0

while win_continuos != 2:
    computer = random.randint(0,3)
    user = eval(input("Enter 0,1 or 2"))
    chosen_value_comp = rockpaperscissor(computer)
    chosen_value_user = rockpaperscissor(user)

    if computer == user:
             win_draw = win_draw + 1
    elif computer > user:

       win_comp += 1
    elif user > computer:

       win_user += 1

    if((win_draw ==1 and win_user==1) or (win_draw==1 and win_comp==1) or (win_comp==1 and win_user==1)):
        win_comp =0
        win_user =0
        win_draw =0
    elif(win_draw == 2 or win_user == 2 or win_comp ==2):
       win_continuos=2

if(win_draw == 2):
    print("Draw")

if(win_user== 2):
    print("user")

if(win_comp == 2):
    print("Comp")

