def printBoard(): #prints the current board, in a grid layout with | between rows.
    print("|".join(board[0]))
    print("|".join(board[1]))
    print("|".join(board[2]))

def playerPlay(player): #player input. doesn't check for an empty space, this is done on the main loop.
    sel = input(f'Player {player}, please enter your selection(row, column):')
    sel.split(",")
    row = int(sel[0])
    column = int(sel[2])
    play = [row, column]
    return play

def changeBoard(currentPlayer, currentPlay): #a function to change the state of a single block. called with the play, and the symbol.
    board[currentPlay[0]][currentPlay[1]] = currentPlayer
    return

def boardCount():   #returns amount of empty spaces. 0 means the board is full, and game is at a draw
    count = 0
    for x in board:
        count += x.count("_")
    return count

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





while True:
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]] #Initialize board
    firstPlayerTurn = True  #1st player is allways X's
    while True:

        printBoard()

        if firstPlayerTurn: #first player is always 'x'. statement checks is it's the first player turn.
            currentPlayer = "x"
            currentPlay = playerPlay(1)
            if board[currentPlay[0]][currentPlay[1]] == "_": #is the spot the player chose empty? if not, restarts the while loop
                changeBoard(currentPlayer, currentPlay)
                firstPlayerTurn = False #flips the player to the second player.
            else:
                print("place taken, please choose another spot")
                continue
        else:
            currentPlayer = "o"
            currentPlay = playerPlay(2)
            if board[currentPlay[0]][currentPlay[1]] == "_":
                changeBoard(currentPlayer, currentPlay)
                firstPlayerTurn = True
            else:
                print("place taken, please choose another spot")
                continue

        win=checkWin() #function to check if any win condition is present. runs after each play.

        if win:  #if True. Win has value 0 (False) if no win condition is met.
            printBoard()
            print(f'Player wins in {win[0]} {win[1]}')  # congratulate
            break # TODO: ogokoeoo



        if boardCount() == 0:   #board full check is below win check. player can win in a full board (last move)
            printBoard()
            print("There are no winners...Better luck next time!")#board is full, a draw
            break

    another = input("Would you like to play another game(y/n)?")
    while another.lower() != "y" and another.lower() != "n":
        print("Invalid input")
        another = input("Would you like to play another game(y/n)?")

    if another.lower() == "y":
        continue

    elif another.lower() == "n":
        print("Thanks for playing!")
        break








# TODO:
#   * implement input cleaning (no illegal input allowed, and won't break the game - critical)
#   * implement PC? 2 PCs?
#   * implement 'next turn can win' scenario
