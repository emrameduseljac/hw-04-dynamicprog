#THIS IS NOT DYNAMIC PROGRAMMING, but hopefully its a start (maybe can add some kind of dictionary to keep track of different max heights? idk lol)

def workout(distance, intList, path, numsMoves):
    if (len(path) == numsMoves): # base case: if the length of the path is equal to the number of moves
        if (distance == 0): # only valid if the length is 0
            return path
        else:
            return "IMPOSSIBLE"
    if (distance < 0):
        return "IMPOSSIBLE"
    else:
        result = workout(distance + intList[len(path)], intList, path + "U", numsMoves)
        if (result != "IMPOSSIBLE"):
            return result   
        if (distance - intList[len(path)] >= 0): # checks if distance would go below 0
            result = workout(distance - intList[len(path)], intList, path + "D", numsMoves)
            if (result != "IMPOSSIBLE"):
                return result

    return "IMPOSSIBLE"

tests = int(input())

for i in range (0,tests):
    numberMoves = int(input())
    moves = input()
    movesList = [int(x) for x in moves.split()]


    result = workout(0, movesList, "",numberMoves )
    print(result)
