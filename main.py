'''clear_screen module import'''
import os
positionlist = [0,1,2,3,4,5,6,7,8]
acceptablepositions = ["0","1","2","3","4","5","6","7","8",]
gameon = True

def display(positions):
    '''
    function that displays the current board
    
    :param positions: list containing the current board positions
    '''
    print("   |   |   ")
    print(f" {positions[0]} | {positions[1]} | {positions[2]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {positions[3]} | {positions[4]} | {positions[5]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {positions[6]} | {positions[7]} | {positions[8]} ")
    print("   |   |   ")
    print("")

def clear_screen():
    '''
    function to clear the current output/display
    '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def playerone_choice():
    '''
    function to grab playerone's decision
    '''
    choiceone = "wrong"
    while choiceone not in acceptablepositions:
        choiceone = input("Player one, please enter an index position (0-8) ")
        if choiceone.isdigit() is False or choiceone not in acceptablepositions:
            print("Sorry, You must choose an index position (0-8)")
    return int(choiceone)

def playertwo_choice():
    """
    function to grab playertwo's decision
    """
    choicetwo = "wrong"
    while choicetwo not in acceptablepositions:
        choicetwo = input("Player two, please enter an index position (0-8) ")
        if choicetwo.isdigit() is False or choicetwo not in acceptablepositions:
            print("Sorry, You must choose a free index position!")
    return int(choicetwo)

def x_adder(choiceint):
    '''
    function that adds an X (playerone) to the board
    
    :param choiceint: the index pick of playerone
    '''
    positionlist[int(choiceint)] = "X"
    acceptablepositions[choiceint] = " "
def o_adder(choiceint):
    '''
    function that adds an O (playertwo) to the board
    
    :param choiceint: the index pick of playertwo
    '''
    positionlist[int(choiceint)] = "O"
    acceptablepositions[choiceint] = " "



def game_on():
    '''
    function that runs at the end of the game to ask the players if they want to play again
    '''
    global gameon
    decision = input("Would you like to play another game? Y or N ")
    decision = decision.upper()
    if decision == "Y":
        gameon = True
    elif decision == "N":
        gameon = False

def continue_game():
    '''
    function that grabs the decision from game_on and processes it further
    '''
    global positionlist, acceptablepositions
    game_on()
    if gameon is False:
        return True
    if gameon is True:
        positionlist = [0,1,2,3,4,5,6,7,8]
        acceptablepositions = ["0","1","2","3","4","5","6","7","8",]
        game()

def win_detector():
    '''
    function to detect a win after every move
    '''
    if ((positionlist[0] == positionlist[1] and positionlist[1] == positionlist[2] and\
         positionlist[0] in ['X', 'O']) or \
        (positionlist[3] == positionlist[4] and positionlist[4] == positionlist[5] and\
        positionlist[3] in ['X', 'O']) or \
        (positionlist[6] == positionlist[7] and positionlist[7] == positionlist[8] and\
        positionlist[6] in ['X', 'O']) or \
        (positionlist[0] == positionlist[3] and positionlist[3] == positionlist[6] and\
         positionlist[0] in ['X', 'O']) or \
        (positionlist[1] == positionlist[4] and positionlist[4] == positionlist[7] and\
         positionlist[1] in ['X', 'O']) or \
        (positionlist[2] == positionlist[5] and positionlist[5] == positionlist[8] and\
         positionlist[2] in ['X', 'O']) or \
        (positionlist[0] == positionlist[4] and positionlist[4] == positionlist[8] and\
         positionlist[0] in ['X', 'O']) or \
        (positionlist[2] == positionlist[4] and positionlist[4] == positionlist[6] and\
         positionlist[2] in ['X', 'O'])):
        if continue_game():
            return True

def draw_detector():
    '''
    function to detect if the game is a draw
    '''
    if set(positionlist) == {"X","O"}:
        print("Its a draw!")
        if continue_game():
            return True




def game():
    '''
    function to sort the logic of the game
    '''
    display(positionlist)
    while gameon is True:
        x_adder(playerone_choice())
        clear_screen()
        display(positionlist)
        if win_detector():
            return
        if draw_detector():
            return
        o_adder(playertwo_choice())
        clear_screen()
        display(positionlist)
        if win_detector():
            return

game()
