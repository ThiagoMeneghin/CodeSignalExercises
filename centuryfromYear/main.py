def centuryFromYear(year):
    sec = year // 100
    if(year % 100 == 0):
        return sec
    else:
        return sec + 1