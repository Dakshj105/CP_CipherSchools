def MatrixSpiralPrint(li):
    r_s = 0
    c_s = 0
    r_e = len(li)
    c_e = len(li[0])

    while(r_s < r_e and c_s < c_e):    
        for i in range(c_s, c_e):
            print(li[r_s][i], end = ' ')
        r_s += 1

        for i in range(r_s, r_e):
            print(li[i][c_e - 1], end = " ")
        c_e -= 1

        for i in range(c_e - 1, c_s - 1, -1):
            print(li[r_e - 1][i], end = " ")
        r_e -= 1

        for i in range(r_e - 1, r_s - 1, -1):
            print(li[i][c_s], end = " ")
        c_s += 1




li = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
MatrixSpiralPrint(li)