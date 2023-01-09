import sys

def main():
    playGame()

def buildBoard():
    lst = ['0', '1', '2', '3','4', '5', '6', '7', '8']
    return lst

def printBoard(board):
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
    board = buildBoard()
    printBoard(board)
    turns = 1
    p1 = set()
    p2 = set()
    check = 'Continue'

    while turns <= 8:
        if len(p1) > 2 or len(p2) > 2:
            check = checkWinner(p1, p2)
            if check != 'Continue':
                print(check)
                break
        turns, board, p1, p2 = player(turns, board, p1, p2)
    else:
        print("The game is a tie!")

def player(turns, board, p1, p2):
    print('turns', turns)
    if turns % 2 != 0 or turns == 1:
        player = 'X'
        value = int(input("Player X, enter a number between 0 to 8: "))
        if value > 8 or value < 0:
            value = int(input("You entered an invalid number, enter a number between 0 to 8: "))
        elif board[value] in ['X', 'O']:
            value = int(input("The cell you picked is already filled, please pick a new number: "))
        p1.add(value)
    else: 
        player = 'O'
        value = computerPlayer(p1, p2, board)
        p2.add(value)
        print('Player O played {0} value'.format(value))

    board[value] = player
    print('p1', p1)
    print('p2', p2)
    turns += 1
    value = None
    printBoard(board)

    return turns, board, p1, p2

def computerPlayer(p1, p2, board):
    # computer player is always O
    # return the value that it will play
    px = p1.copy()
    po = p2.copy()
    # if computer player wins on next game play that one
    print(id(px) == id(p1))
    for value in range(len(board)):
        if board[value] not in ['X', 'O']:
            po.add(value)
            if len(po) >= 3:
                check = checkWinner(px, po)
                if check == "!!! Player 2 won the game !!!":
                    return value
            else:
                po.remove(value)
    # else block X
    for value in range(len(board)):
        if board[value] not in ['X', 'O']:
            px.add(value)
            if len(px) >= 3:
                check = checkWinner(px, po)
                if check == "!!! Player 1 won the game !!!":
                    return value
            else:
                px.remove(value)
    # else fill the middle
    if board[4] == '4':
        return 4
    else:
        for value in range(len(board)):
            if board[value] not in ['X', 'O']:
                return value

    

def checkWinner(p1, p2):
    pattern = 0
    check = None
    patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    while not check and pattern < 8:
        if set(patterns[pattern]).issubset(p1):
            check = "!!! Player 1 won the game !!!"
            return check
        if set(patterns[pattern]).issubset(p2):
            check = "!!! Player 2 won the game !!!"
            return check

        pattern += 1

    if not check:
        check = "Continue"
        return check


if __name__ == "__main__":
    main()
