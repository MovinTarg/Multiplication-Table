def mTable(max):
    newStr = 'x '
    for x in range (1, max+1):
        newStr += str(x)+' '
    print newStr
    for column in range (1, max+1):
        for row in range (1, max+1):
            print column*row, '\t',
        print '\n',  
mTable(12)