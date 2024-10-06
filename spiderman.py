#THIS IS NOT DYNAMIC PROGRAMMING, but hopefully its a start (maybe can add some kind of dictionary to keep track of different max heights? idk lol)

def spiderman(climbList):
    solutions = []
    stack = [(0, 0, "")]  # (currentHeight, maxHeight, path)
    
    while len(stack) != 0:
        currentHeight, maxHeight, moves = stack.pop()
        
        if len(moves) == len(climbList):
            if currentHeight == 0:
                solutions.append((moves, maxHeight)) #once it reaches the length of the climb list it
        else:
            upHeight = currentHeight + climbList[len(moves)]
            upMaxHeight = max(upHeight, maxHeight)
            stack.append((upHeight, upMaxHeight, moves + "U"))

            downHeight = currentHeight - climbList[len(moves)]
            if downHeight >= 0:
                stack.append((downHeight, maxHeight, moves + "D"))
    if len(solutions) == 0: # figures out if there are no valid solutions
        return "IMPOSSIBLE"
    bestSol = ''
    bestNum = float('inf')
    for curSol, curNum in solutions: #finds best solution
        if curNum < bestNum:
            bestSol = curSol
            bestNum = curNum

    return bestSol
tests = int(input())
for i in range (0, tests):
    num = int(input())
    moves = input()
    movesList = [int(x) for x in moves.split()]
    print(spiderman(movesList))
