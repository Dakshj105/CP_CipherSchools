def SearchElementSortedMatrix(matrix, element):
    i1 = 0
    i2 = len(matrix[0]) - 1
    while(i1 < len(matrix[0]) and i2 >= 0):
        if matrix[i1][i2] == element:
            return (i1, i2)
        elif matrix[i1][i2] < element:
            i1 += 1
        else:
            i2 -= 1
    return "Element not found"

matrix = [[1, 3, 5, 7], [2, 4, 6, 8], [9, 11 ,13, 15], [10, 12, 14, 16]]
element = int(input())
print(SearchElementSortedMatrix(matrix, element))