def makeArrayConsecutive2(statues):
    statues.sort()
    ant = None
    nostatues = 0
    for statue in statues:
        if ant is not None and statue - ant == 1:
            pass
        elif ant is not None:
            nostatues += statue - ant - 1
        ant = statue
    return nostatues