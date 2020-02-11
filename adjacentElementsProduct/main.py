def adjacentElementsProduct(inputArray):
    ant = None
    maxprod = -100000000
    for x in inputArray:
        if(ant is not None and x * ant > maxprod):
            maxprod = x * ant
        ant = x
    return maxprod