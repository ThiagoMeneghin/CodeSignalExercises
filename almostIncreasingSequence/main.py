def almostIncreasingSequence(sequence):
    ant = None
    mark = 0
    for x in sequence:
        if ant is None or x > ant:
            pass
            print("Pass")
        else:
            mark += 1
            print("Marked")
        ant = x
        print(ant)
    
    if mark > 1:
        return False
    else:
        return True

sequence = [40, 50, 60, 10, 20, 30]
print(almostIncreasingSequence(sequence))

#Not finished