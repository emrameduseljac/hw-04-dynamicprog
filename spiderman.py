def printTable(table):
    for j in range (len(table)):     #this was for testing
        print("Row ", j+1)
        for i in range (len(table[j])):       
            if table[j][i] != False:
                print(i) 

def spiderman(climbList, size):
    size = len(climbList)
    maxi = (sum(climbList))//2
    table = [[False] * (maxi + 1) for i in range(size + 1)]
    table[0][0] = True

    for i in range(1, size + 1):
        dDistance = climbList[i - 1]
        for j in range(maxi + 1):
            if table[i - 1][j] != False:
                if j + dDistance <= maxi:
                    table[i][j + dDistance] = True #fills out table of valid places
                if j - dDistance >= 0:
                    table[i][j - dDistance] = True #fills out table of valid places
    if table[size][0] != True: #if touching the ground isnt possible it returns impossible
        return "IMPOSSIBLE"
    else: # backtracks to find path
        path = ""
        distance = 0
        for i in range(size, 0, -1):
            jump = climbList[i - 1]
            if (distance - jump >= 0 and table[i - 1][distance - jump]): #tries to stay as close to the ground as possible while backtracking solutions
                path = 'U' + path
                distance -= jump
            else:
                path = 'D' + path
                distance += jump
            print(distance)

    return path
tests = int(input())
for i in range(tests):
    size = int(input())
    climbS = input()
    climbList = [int(num) for num in climbS.split()]
    print(spiderman(climbList, size))
    
