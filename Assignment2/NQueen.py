def NQueen(n):
    result = []
    SolveNQueen(0, n, [], result)
    for i in result:
        for j in i:
            print(j)
        print()
    return

def SolveNQueen(row, n, col,  result):
    if row == n:
        result.append(__boardGenerator__(col, n))
        result

    for j in range(n):
        col.append(j)
        
        if __isValid__(col):
            SolveNQueen(row + 1, n, col, result)

        col.pop()

def __isValid__(col):
    row = len(col) - 1
    for i in range(row):
        d_col = abs(col[i] - col[row])
        d_row = row - i
        if d_col == 0 or d_col == d_row:
            return False
    return True

def __boardGenerator__(col, n):
    board = []
    itemsPlaced = len(col)

    for row in range(itemsPlaced):
        line = ''
        for column in range(itemsPlaced):
            if column == col[row]:
                line += "Q"

            else:
                line += "."

        board.append(line)

    return board

n = int(input())
NQueen(n)





