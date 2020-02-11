def shapeArea(n):
    if n == 1:
        return 1
    aux = 0
    for x in range(1, n):
        aux += x * 4
    area = 1 + aux
    return area