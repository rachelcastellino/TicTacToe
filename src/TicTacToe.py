import sys

def main():
    playGame()

def buildBoard():
    # the players don't see this but this is a flattened playing board where values will be updated
    lst = ['0', '1', '2', '3','4', '5', '6', '7', '8']
    return lst

def printBoard(board):
    # makes the board you see to play on
    row = ''
    for n in range(len(board)):
        row += board[n]
        if n not in [2, 5, 8]:
            row += ' | '
        else:
            print(row.rstrip())
            if n != 8:
                print('---------')
            row = ''



def playGame():
    # this is the primary function that calls the player or the GUI to play
    # a tie will happen if there have been 8 turns played but no one has won yet
    board = buildBoard()
    printBoard(board)

    turns = 1
    user, computer = set(), set()
    check = 'Continue'

    while turns <= 8:
        if len(user) > 2 or len(computer) > 2:
            check = checkWinner(user, computer)
            if check != 'Continue':
                print(check)
                break
        turns, board, user, computer = player(turns, board, user, computer)
    else:
        print("The game is a tie!")

def player(turns, board, user, computer):
    # player is called to enter in a value input and the board is updated if valid value
    # the GUI is called afterwards
    if turns % 2 != 0 or turns == 1:
        player = 'X'
        value = int(input("Player X, enter a number between 0 to 8: "))
        # invalid character
        if value > 8 or value < 0:
            value = int(input("You entered an invalid number, enter a number between 0 to 8: "))
        elif board[value] in ['X', 'O']:
            value = int(input("The cell you picked is already filled, please pick a new number: "))
        user.add(value)
    else: 
        player = 'O'
        value = computerPlayer(user, computer, board)
        computer.add(value)
        print('Player O played {0} value'.format(value))

    board[value] = player
    turns += 1
    value = None
    printBoard(board)

    return turns, board, user, computer

def computerPlayer(user, computer, board):
    # the GUI first checks to see if it can win or block
    userCopy, computerCopy = user.copy(), computer.copy()
    for value in range(len(board)):
        if board[value] not in ['X', 'O']:
            computerCopy.add(value)
            userCopy.add(value)
            if len(userCopy) >= 3 or len(computerCopy) >= 3:
                check1, check2 = checkWinner(computerCopy, computer), checkWinner(user, userCopy)
                if check1 == "!!! Player 1 won the game !!!":
                    return value
                elif check2 == "!!! Player 2 won the game !!!":
                    return value
                else:
                    userCopy.remove(value)
                    computerCopy.remove(value)
    if board[4] == '4':
        return 4
    else:
        for value in range(len(board)):
            if board[value] not in ['X', 'O']:
                return value

    

def checkWinner(user, computer):
    pattern = 0
    check = None
    patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    while not check and pattern < 8:
        if set(patterns[pattern]).issubset(user):
            check = "!!! Player 1 won the game !!!"
            return check
        if set(patterns[pattern]).issubset(computer):
            check = "!!! Player 2 won the game !!!"
            return check

        pattern += 1

    if not check:
        check = "Continue"
        return check


if __name__ == "__main__":
    main()
