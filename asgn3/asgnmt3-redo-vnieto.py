import random
import math

def step(prob):
    rand = random.randrange(0, 100)
    if rand <= prob:
        return 1

    else:
        return -1




def randomWalk(min, max, prob, start):
    position = start
    leftWalk = 0
    rightWalk = 0
    numSteps = 0
    maxWalk = 0
    data = []
    while numSteps < 5000:

        if position <= min:
            break
        elif position >= max:
            break

        #position = step(position, prob)
        direction = step(prob)
        if direction == 1:
            position += 1
            numSteps += 1
        elif direction == -1:
            position -= 1
            numSteps += 1

        if numSteps == 5000:
            maxWalk += 1
    if position > start:
        rightWalk += 1
    if position < start:
        leftWalk += 1

    data.append(numSteps)
    data.append(leftWalk)

    return data


def walkSimulator():
    start = int(input("What is the start location (1-499)? "))
    x = start + 1
    y = start - 1
    max = int(input("What is the maximum value (" + str(x) + "-500)? "))

    min = int(input("What is the minimum value (0-" + str(y) + ")? "))

    probRight = int(input("What is the percentage chance of moving right (1-99)? "))

    numWalks = int(input("How many walks? "))

    print()

    leftSteps = 0
    rightSteps = 0
    left = 0
    right = 0
    maxStep = 0
    left_mean = 0.0
    right_mean = 0.0
    left_variance = 0.0
    right_variance = 0.0
    left_sum_sq_diff = 0.0
    right_sum_sq_diff = 0.0
    left_std_dev = 0.0
    right_std_dev = 0.0


    for i in range(numWalks):
        data = randomWalk(min, max, probRight, start)
        if data[1] == 1:
            left += 1
            leftSteps += data[0]
            delta = data[0] - left_mean
            left_mean += delta / left
            if left > 2:
                left_sum_sq_diff += delta*(data[0] - left_mean)

            left_variance = left_sum_sq_diff / left
            left_std_dev = math.sqrt(left_variance)

        elif data[1] == 0:
            right += 1
            rightSteps += data[0]
            delta = data[0] - right_mean
            right_mean += delta / right
            if right > 2:
                right_sum_sq_diff += delta * (data[0] - right_mean)

            right_variance = right_sum_sq_diff / right
            right_std_dev = math.sqrt(right_variance)
        total_variance = left_variance + right_variance
        total_std_dev = math.sqrt(total_variance)

        if data[0] == 5000:
            maxStep += 1
    totalSteps = leftSteps + rightSteps
    totalMean = float(totalSteps) / numWalks

    # check to see if there are walks that ended on the left
    # if there are calculate the left mean
    if left > 0:
        left_mean = float(leftSteps) / left
    else:
        left_mean = 0

    if right > 0:
        right_mean = float(rightSteps) / right
    else:
        right_mean = 0

    print("Walks that ended on the left: " + "\n Number of walks: " + str(left))
    print(" Mean number of steps per walk: " + str(left_mean))
    print(" Standard deviation of number of steps per walk: " + str(left_std_dev))
    print()
    print("Walks that ended on the right: " + "\n Number of walks: " + str(right))
    print(" Mean number of steps per walk: " + str(right_mean))
    print(" Standard deviation of number of steps per walk: " + str(right_std_dev))
    print()
    print("Walks that hit 5000 steps: " + str(maxStep))
    print(" Mean number of steps per walk: 5000.0" + " \n Standard deviation of number of steps per walk: 0.0 ")
    print()
    print("All walks: \n Number of walks: " + str(numWalks) + "\n Mean number of steps per walk: " + str(totalMean))
    print(" Standard deviation of number of steps per walk: " + str(total_std_dev))



walkSimulator()

#data = randomWalk(100, 300, 51, 200)
#for i in data:
    #print(str(i))
