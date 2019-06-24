def printBoard(): #prints the current board, in a grid layout with | between rows.
    print("|".join(board[0]))
    print("|".join(board[1]))
    print("|".join(board[2]))

def playerPlay(player): #player input. doesn't check for an empty space, this is done on the main loop.
    while True:
        sel = input(f'Player {player}, please enter your selection(row, column):')
        sel.split(",")
        if sel[0] not in ("1","2","3") or sel[2] not in ("1","2","3"):   #input filtering - if invalid, repeats question
            print("input invalid")
            continue
        row = int(sel[0])-1 #this and below correct for off-by-one error, and split to row and column for better readability
        column = int(sel[2])-1
        play = [row, column]
        break

    return play

def changeBoard(currentPlayer, currentPlay): #a function to change the state of a single block. called with the play, and the symbol.
    board[currentPlay[0]][currentPlay[1]] = currentPlayer
    return

def boardCount():   #returns amount of empty spaces. 0 means the board is full, and game is at a draw
    count = 0
    for x in board:
        count += x.count("_")
    return count


'''
old version of checkWin()

def checkWin(): #a function to check all win states (rows, colums, diagonals)
    # check rows
    i = 0
    for row in board:   #just wanted to play around, couldnt figure a clean way to do columns the same
        xs = row.count("x")
        os = row.count("o")
        i+=1
        if xs == 3 or os == 3:
            return ("row",i)
        # check columns
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != "_":
        return ("column",1)
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != "_":
        return ("column",2)
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != "_":
        return ("column",3)
        #check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != "_":
        return ("Diagonal", "LtR")
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != "_":
        return ("Diagonal", "RtL")
    else: return 0
'''


def checkWin():
    i=0
    for row in board:  # checks rows
        xs = row.count("x")
        os = row.count("o")
        i += 1
        if xs == 3 or os == 3:
            return ("row", i)

    for colCount in range(3): #cleaner way for checking columns

        i=0
        for row in board:
            test = board[0][colCount] #sets test as the top tile of the column
            if row[colCount] == test and row[colCount] != "_": #checks each tile in the column against the top tile in that column (minus empty tiles)
                i+=1
        if i == 3: #number of the same tiles in a column. if 3, it's a win.
            return ("column", colCount+1)

    #check diagonals. don't think a more 'program-y' version will be actually better
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != "_":
        return ("Diagonal", "LtR")
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != "_":
        return ("Diagonal", "RtL")
    else: return 0


def initNewGame():
    global playerNumber     #not sure what's going on. for some reason board clean-up worked without global...I think.
    global humanPlayers
    global board
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]  # Initialize board
    playerNumber = 0  # 1st player is allways X's
    while True:
        humanPlayers = input("How many human players?")
        if humanPlayers in ("0","1","2"):
            humanPlayers = int(humanPlayers)
            break
        else:
            print("Invalid Input")
            continue

def isEmpty(currentPlay):
    if board[currentPlay[0]][currentPlay[1]] == "_": #checks if the current play is an empty tile.
        return True
    else: return False

import random

def pcPlay(player): #a function that randomly selects an empty tile. used for the PC player's turn
    while True:
        sel = [random.randint(0,2),random.randint(0,2)]
        row = int(sel[0])
        column = int(sel[1])
        play = [row, column]
        if not isEmpty(play): #if the return from isEmpty() is False, return to start
            continue
        else:
            print(f'PC Player {player-2} has played:')
            break
        
    return play

def changePlayer(): #changes the current player. if two humans - between 1 and 2, if 2 pc's - between 3 and 4. if one human, between 1 and 4 (x's vs o's)
    global playerNumber
    if humanPlayers == 2:
        if playerNumber == 1: playerNumber = 2
        else: playerNumber = 1
    if humanPlayers == 1:
        if playerNumber == 1: playerNumber = 4
        else: playerNumber = 1
    if humanPlayers == 0:
        if playerNumber == 3: playerNumber = 4
        else: playerNumber = 3

####### Start

#Initial variables
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]  # Initialize board
playerNumber = 0  # 1st player is allways X's
humanPlayers = 2

#Main loop
while True:
    initNewGame()   #moved this to a function for a cleaner look. refreshes the board and game state.
    changePlayer()  #makes the first player to player 1 if vs human or PC, makes it player 3(pc) if only PC's are playing
    while True:

        printBoard()

        if playerNumber == 1: #first player is always 'x'. statement checks is it's the first player turn.
            currentPlayer = "x"
            currentPlay = playerPlay(1) #call to the play function - input from the player and input filtering
            if isEmpty(currentPlay):
                changeBoard(currentPlayer, currentPlay)
                #changePlayer()
            else:
                print("place taken, please choose another spot")
                continue


        elif playerNumber == 2 :
            currentPlayer = "o"
            currentPlay = playerPlay(2)
            if isEmpty(currentPlay):
                changeBoard(currentPlayer, currentPlay)
                #changePlayer()
            else:
                print("place taken, please choose another spot")
                continue


        elif playerNumber == 3:
            currentPlayer = "x"
            currentPlay = pcPlay(3)  # call to the pc play function - random input
            changeBoard(currentPlayer, currentPlay) #pcPlay() only places in non empty spots
            #changePlayer()


        elif playerNumber == 4:
            currentPlayer = "o"
            currentPlay = pcPlay(4)  # call to the pc play function - random input
            changeBoard(currentPlayer, currentPlay)  # pcPlay() only places in non empty spots
            #changePlayer()

        win=checkWin() #function to check if any win condition is present. runs after each play.

        if win:  #if True. Win has value 0 (False) if no win condition is met.
            printBoard()
            if playerNumber in (3,4):
                print(f'PC Player {playerNumber}({currentPlayer}) wins in {win[0]} {win[1]}')  # congratulate
            else:
                print(f'Player {playerNumber}({currentPlayer}) wins in {win[0]} {win[1]}')  # congratulate
            break


        changePlayer()



        if boardCount() == 0:   #board full check (draw). Is below win check- player can win in a full board (last move)
            printBoard()
            print("There are no winners...Better luck next time!")#board is full, a draw
            break


    #new game loop. checks if input is valid (Y,y,N,n). if not, repeats question.

    another = input("Would you like to play another game(y/n)?")
    while another.lower() != "y" and another.lower() != "n":    #input filter for only valid input.
        print("Invalid input")
        another = input("Would you like to play another game(y/n)?")

    if another.lower() == "y": #repeats main game loop
        continue

    elif another.lower() == "n":
        print("Thanks for playing!")
        break








# TODO:
#   * implement 'next turn can win' scenario
