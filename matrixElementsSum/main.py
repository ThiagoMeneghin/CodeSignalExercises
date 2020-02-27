matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]

def matrixElementsSum(matrix):
    row = len(matrix)
    column = len(matrix[0])
    sum = 0
    
    for x in range(row):
        for y in range(column):
            if matrix[x][y] > 0:
                stop = x
                haunt = False
                while haunt == False and stop > 0:
                    if matrix[stop - 1][y] == 0:
                        haunt = True
                    stop -= 1
                if haunt == False:
                    sum += matrix[x][y]
                    print(matrix[x][y])
    
    return sum

print(matrixElementsSum(matrix)) 


