import random
start = input("What is the start location (1-499)? ")
start = int(start)
position = start
x = start + 1
y = start - 1
max = int(input("What is the maximum value (" + str(x) + "-500)? "))

min = int(input("What is the minimum value (0-" + str(y) + ")? "))

probRight = int(input("What is the percentage chance of moving right (1-99)? "))

numWalks = int(input("How many walks? "))




def walkSimulator(num):
    rightStep = 0
    leftStep = 0
    rightWalk = 0
    leftWalk = 0
    for i in range(1, num):
        data = randomWalk(min, max, probRight)
        rightWalk += data[2]
        leftWalk = data[1]
        steps = data[0]
        if (temp1 + 1) == rightWalk:
            rightStep += steps
        elif (temp2+1) == leftWalk:
            leftStep += steps
        else:

        steps = 0

    meanStepsR = float(rightStep)/rightWalk
    meanStepsL = float(leftStep)/leftWalk
    print("Walks that ended on the left: /n" + str(leftWalk) + "/n" + "Mean number of steps per walk: " + str(meanStepsL) + "/n")
    print("Walks that ended on the right: /n" + str(rightWalk) + "/n" + "Mean number of steps per walk: " + str(meanStepsR) + "/n")


def randomWalk(min, max, prob):
    leftWalk = 0
    rightWalk = 0
    numSteps = 0
    position = start
    data = []
    while numSteps < 5000:

        if position <= min:
            break
        elif position >= max:
            break

        numSteps = step(position, prob, numSteps)

    if position > start:
        rightWalk += 1
    elif start > position:
        leftWalk += -1

    data.append(numSteps)
    data.append(leftWalk)
    data.append(rightWalk)

    return data



def step(position, prob, numSteps):
    prob = float(prob)/100;
    rand = random.random();
    if rand <= prob:
        position += 1
        numSteps += 1
    elif rand > prob:
        position += -1
        numSteps += 1
    return numSteps


walkSimulator(numWalks)
