def firstNotRepeatingCharacter(s):

    dict = {}
    found = 0

    for elem in s:
        if elem in dict:
            dict[elem] +=1
        else:
            dict[elem] = 1   
    for x in dict:
        if dict[x] == 1:
            print(x)
            break



