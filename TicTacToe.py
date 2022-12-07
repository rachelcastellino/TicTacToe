import sys


def main():
    playGame()

# ways to make better
# refactor to combine player functions

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
    player = 0
    p1 = set()
    p2 = set()
    value = None
    check = 'Continue'

    if turns >= 3 and turns < 8:
        check = checkWinner(p1, p2)

    while turns < 8:
        if turns >= 6:
            check = checkWinner(p1, p2, board)
            if check != 'Continue':
                return check

        if turns % 2 != 0 or turns == 1:
            if value is None:
                value = int(input("Player 1, enter a number between 0 to 8: "))

            if value > 8 or value < 0:
                value = int(input("You entered an invalid number, enter a number between 0 to 8: "))
            else:
                if board[value] not in ['X', 'O']:
                    p1.add(value)
                    board[value] = 'X'
                    turns += 1
                    value = None
                    printBoard(board)
                else:
                    value = int(input("The cell you picked is already filled, please pick a new number: "))

        else:
            if value is None:
                value = int(input("Player 2, enter a number between 0 to 8: "))
            if value > 8 or value < 0:
                value = int(input("You entered an invalid number, enter a number between 0 to 8: "))
            else:
                if board[value] not in ['X', 'O']:
                    p2.add(value)
                    board[value] = 'O'
                    turns += 1
                    value = None
                    printBoard(board)
                else:
                    value = int(input("The cell you picked is already filled, please pick a new number: "))
    else:
        check = "The game is a tie!"
        print(check)

    return check

def checkWinner(p1, p2, board):
    pattern = 0
    output = None
    patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    while output is None and pattern <8:
        if set(patterns[pattern]).issubset(p1):
            output = "Player 1 won the game"
            break
        if set(patterns[pattern]).issubset(p2):
            output = "Player 2 won the game"
            break
        pattern += 1

    if output is None:
        output = "Continue"
    else:
        print(output)
        printBoard(board)
    return output


if __name__ == "__main__":
    main()
