def spiderman(climbList, size):
    max = sum(climbList)
    table = [[False] * (max + 1) for i in range(size + 1)]
    table[0][0] = ""

    for i in range(1, size + 1):
        dDistance = climbList[i - 1]
        for j in range(max + 1):
            if table[i - 1][j] != False:
                if j + dDistance <= max:
                    table[i][j + dDistance] = True #fills out table of valid places
                if j - dDistance >= 0:
                    table[i][j - dDistance] = True #fills out table of valid places
    if table[size][0] != True: #if touching the ground isnt possible it returns impossible
        return "IMPOSSIBLE"
    else:
        return "path"
    #for j in range (len(table)):     #this was for testing
    #    print("Row ", j+1)
    #    for i in range (len(table[j])):
    #        
    #        if table[j][i] == True:
    #            print(i)

print(spiderman([20,20,20,20], 4))


