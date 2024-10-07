def trainsorting(numOfCars, weightOfCars):
    # initialize increasing and decreasing lists of subsequence lengths
    increasing = []
    decreasing = []
    # set min. subsequence lengths to 1
    for i in range(numOfCars):
        increasing.append(1)
        decreasing.append(1)
    # check if current car heavier than previous car(s)
    for curr_car in range(numOfCars):
        for prev_car in range(i):
            if weightOfCars[curr_car] > weightOfCars[prev_car]:
                # if weight of current car is heavier than weight of a previous car, add 1 to length of current car
                increasing[curr_car] = increasing[prev_car]+1       
    # start from last car to compare with future car(s)
    for curr_car in reversed(range(numOfCars)):
        for future_car in range(curr_car + 1, numOfCars):
            if weightOfCars[curr_car] > weightOfCars[future_car]:
                # if weight of current car greater than weight of future car, add 1 to length of current car
                decreasing[curr_car] = decreasing[future_car]+1
    # outputs number of cars in the longest train that can be made given the restrictions
    max_length = 0
    for i in range(numOfCars):
        max_length = increasing[i] + decreasing[i] - 1
    return max_length
    
# input
numOfCars = int(input())
weightOfCars = []
for i in range(numOfCars):
    weight = int(input())
    weightOfCars.append(weight)
print(trainsorting(numOfCars, weightOfCars))