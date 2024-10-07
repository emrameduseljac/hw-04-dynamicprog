def trainsorting(numOfCars, weightOfCars):
    # Decreasing and increasing lists to store lengths of subsequences
    decreasing = [1] * numOfCars
    increasing = [1] * numOfCars

    # Calculate decreasing subsequence length from each position
    for i in range(numOfCars - 2, -1, -1):
        for j in range(i + 1, numOfCars):
            if weightOfCars[i] > weightOfCars[j]:
                decreasing[i] = max(decreasing[i], 1 + decreasing[j])

    # Calculate increasing subsequence length from each position
    for i in range(numOfCars - 2, -1, -1):
        for j in range(i + 1, numOfCars):
            if weightOfCars[i] < weightOfCars[j]:
                increasing[i] = max(increasing[i], 1 + increasing[j])

    # Calculate the maximum length of the train
    max_length = 0
    for i in range(numOfCars):
        max_length = max(max_length, decreasing[i] + increasing[i] - 1)

    return max_length

# Input
numOfCars = int(input())
weightOfCars = []
for i in range(numOfCars):
    weight = int(input())
    weightOfCars.append(weight)

print(trainsorting(numOfCars, weightOfCars))
