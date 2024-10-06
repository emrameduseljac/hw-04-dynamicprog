def spiderman(climbList, size):
    total = sum(climbList)
    maxi = total
    inf = float('inf')


    table = [[inf] * (maxi + 1) for _ in range(size + 1)]
    decisions = [[0] * (maxi + 1) for _ in range(size + 1)]

    table[0][0] = 0

    if total % 2 == 1:
        return "IMPOSSIBLE"

    for i in range(1, size + 1):
        dDistance = climbList[i - 1]
        for j in range(maxi + 1):
            if table[i - 1][j] != inf:
                new_h = j + dDistance
                if new_h <= maxi:
                    new_max_h = max(table[i-1][j], new_h)
                    if new_max_h < table[i][new_h]:
                        table[i][new_h] = new_max_h
                        decisions[i][new_h] = 1
                new_h = j - dDistance
                if new_h >= 0:
                    new_max_h = table[i-1][j]
                    if new_max_h < table[i][new_h]:
                        table[i][new_h] = new_max_h
                        decisions[i][new_h] = -1
                
    if table[size][0] == inf:
        return "IMPOSSIBLE"
    
    # backtracks to find path
    path = ""
    h = 0
    for i in range(size, 0, -1):
        decision = decisions[i][h]
        if decision == 1:
            path = "U" + path
            h -= climbList[i - 1]
        elif decision == -1:
            path = "D" + path
            h += climbList[i - 1]
        else:
            return "IMPOSSIBLE"

    return path

tests = int(input())
for _ in range(tests):
    size = int(input())
    climbS = input()
    climbList = [int(num) for num in climbS.split()]
    print(spiderman(climbList, size))
