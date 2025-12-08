import os
positionlist = [0,1,2,3,4,5,6,7,8]
acceptablepositions = ["0","1","2","3","4","5","6","7","8",]
gameon = True

def display(positionlist):
    print("   |   |   ")
    print(f" {positionlist[0]} | {positionlist[1]} | {positionlist[2]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {positionlist[3]} | {positionlist[4]} | {positionlist[5]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {positionlist[6]} | {positionlist[7]} | {positionlist[8]} ")
    print("   |   |   ")
    print("")
    
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def playerone_choice():
    choiceone = "wrong"
    while choiceone not in acceptablepositions:
        choiceone = input("Player one, please enter an index position (0-8) ")
        if choiceone.isdigit() == False or choiceone not in acceptablepositions:
            print("Sorry, You must choose an index position (0-8)")
    return int(choiceone)
 
def playertwo_choice():
    choicetwo = "wrong"
    while choicetwo not in acceptablepositions:
        choicetwo = input("Player two, please enter an index position (0-8) ")
        if choicetwo.isdigit() == False or choicetwo not in acceptablepositions:
            print("Sorry, You must choose a free index position!")
    return int(choicetwo)

def x_adder(choiceint):
    positionlist[int(choiceint)] = "X"
    acceptablepositions[choiceint] = " "
def o_adder(choiceint):
    positionlist[int(choiceint)] = "O"
    acceptablepositions[choiceint] = " "

def game_on():
    global gameon
    decision = input("Would you like to play another game? Y or N ")
    decision.upper()
    if decision == "Y":
        gameon = True
    elif decision == "N":
        gameon = False

def continue_game():
    global positionlist, acceptablepositions
    game_on()
    if gameon == False:
        return True
    elif gameon == True:
        positionlist = [0,1,2,3,4,5,6,7,8]
        acceptablepositions = ["0","1","2","3","4","5","6","7","8",]
        game()

def win_detector():
    if ((positionlist[0] == positionlist[1] and positionlist[1] == positionlist[2] and positionlist[0] in ['X', 'O']) or \
           (positionlist[3] == positionlist[4] and positionlist[4] == positionlist[5] and positionlist[3] in ['X', 'O']) or \
           (positionlist[6] == positionlist[7] and positionlist[7] == positionlist[8] and positionlist[6] in ['X', 'O']) or \
           (positionlist[0] == positionlist[3] and positionlist[3] == positionlist[6] and positionlist[0] in ['X', 'O']) or \
           (positionlist[1] == positionlist[4] and positionlist[4] == positionlist[7] and positionlist[1] in ['X', 'O']) or \
           (positionlist[2] == positionlist[5] and positionlist[5] == positionlist[8] and positionlist[2] in ['X', 'O']) or \
           (positionlist[0] == positionlist[4] and positionlist[4] == positionlist[8] and positionlist[0] in ['X', 'O']) or \
           (positionlist[2] == positionlist[4] and positionlist[4] == positionlist[6] and positionlist[2] in ['X', 'O'])):
            if continue_game():
                return True


def game():
    display(positionlist)
    while gameon == True:
        x_adder(playerone_choice())
        clear_screen()
        display(positionlist)
        if win_detector():
            return
        o_adder(playertwo_choice())
        clear_screen()
        display(positionlist)
        if win_detector():
            return
        
game()
