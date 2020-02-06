a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
def rotateImage(a):   
    h = len(a)
    matrix = [[0 for x in range(h)] for y in range(h)] 
    print(matrix)
    for x in range(h):
        for y in range(h):
            if y == 0:
                i = 0
            matrix[i][h -(x + 1)] = a[x][y]
            i += 1
    return matrix
mat = rotateImage(a)
print(mat)