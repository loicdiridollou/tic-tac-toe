import random

board = ['-' for _ in range(10)]


def print_board(bo):
    for i in range(1, len(bo)):
        if i%3 == 1 and i != 1:
            print()
        print(bo[i]+' ', end='')
    print()


def space_is_free(pos):
    return board[pos] == '-'

def winner(bo, le):
    return (bo[7] == bo[9] == bo[9] == le) or \
        (bo[4] == bo[5] == bo[6] == le) or \
        (bo[1] == bo[2] == bo[3] == le) or \
        (bo[1] == bo[4] == bo[7] == le) or \
        (bo[2] == bo[5] == bo[8] == le) or \
        (bo[3] == bo[6] == bo[9] == le) or \
        (bo[1] == bo[5] == bo[9] == le) or \
        (bo[3] == bo[5] == bo[7] == le)

def isBoardFull(board):
    return board.count('-') < 2


def select_random(lst):
    return lst[random.randrange(0, len(lst))]
    

def insertLetter(le, pos):
    board[pos] = le


def player_move():
    run = True
    while run:
        move = input('Select a position to put an x')
        try:
            move = int(move)
            if move in range(1, 10):
                if space_is_free(move):
                    run = False
                    insertLetter('x', move)
        except:
            print('Input not accepted')



def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == '-' and x != 0]
    move = 0
    
    for let in ['x', 'o']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move
    
    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            edges_open.append(i)
    
    if len(edges_open) > 0:
        move = select_random(edges_open)
        return move

    return 0
    
def main():
    print_board(board)

    while not isBoardFull(board):
        if not winner(board, 'o'):
            player_move()
            print_board(board)
        else:
            print('Game won by o')
            return

        if not winner(board, 'x'):
            move = comp_move()
            if move == 0:
                print('Tie Game!')
                return
            else:
                insertLetter('o', move)
            print_board(board)
        else:
            print('Game won by x')
            return
        
    if isBoardFull(board):
        print('Tie game')

    

main()