
def check_correctness(number, posi, posj, board):
    for i in range (9):
        if i is not posi:
            if board[i][posj] == number:
                return False
    for j in range(9):
        if j is not posj:
            if board[posi][j] == number:
                return False
    bigi=(posi//3)*3
    bigj = (posj//3)*3
    for i in range(bigi,bigi+3):
        for j in range(bigj, bigj + 3):
            if i is not posi and j is not posj:
                if board[i][j] == number:
                    return False
    return True


def solve(number, posi, posj, board):
    print(posi,posj, number)
    if not check_correctness(number, posi, posj, board):
        return False
    board[posi][posj] = number

    empty_space = False
    for i in range (0,9):
        for j in range(0,9):
            if board[i][j]:
                continue
            empty_space+=1
            for k in range(1, 10):
                if solve(k, i, j, board):
                    #print(posi, posj)
                    return True
            board[posi][posj] = 0
            return False
    if empty_space:
        board[posi][posj] = 0
        return False
    else:
        #print(posi, posj)
        return True


def main():
    board = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0],
    ]
    board = [
        [0, 2, 0, 6, 0, 8, 0, 0, 0],
        [5, 8, 0, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [3, 7, 0, 0, 0, 0, 5, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 0, 1, 3],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 8, 0, 0, 0, 3, 6],
        [0, 0, 0, 3, 0, 6, 0, 9, 0],
    ]

    print(board[0])

    for i in range(1,10):
        if solve(i, 0, 0, board):
            print("hola")
            break

    for i in board:
        print(i)


main()