import numpy as np
import random
import math
import matplotlib.pyplot as plt


def readFromFile():
    inputFile = open("input.in", "r")

    # capacity -> the knapsack capacity.
    global capacity
    capacity = int(inputFile.readline())

    # weights -> the weights of the objects.
    global weights
    weights = [int(wt) for wt in inputFile.readline().split(",")]

    # profits -> the profits of each object.
    global profits
    profits = [int(pf) for pf in inputFile.readline().split(",")]

    global optimal_select,num_object,maxProfit
    # optimal_select -> the optimal selection of weights
    optimal_select = [int(os) for os in inputFile.readline().split(",")]
    # maxProfits -> 在optimal selection下的最大profit總和
    maxProfit = np.dot(optimal_select,profits)
    # num_object -> 總共有多少個object
    num_object = len(optimal_select)
    inputFile.close()

#計算所有object的weight總和
def checkMaxWeight():
    MaxWeight = 0
    for i in range(len(weights)):
        MaxWeight += weights[i]

    return MaxWeight

#random挑選一個object的position，將其從 0變1 or 1變0
def FlipOnePosition(s):
    position = random.randint(0, num_object - 1)
    if s[position] == 0:
        s[position] = 1
    else:
        s[position] = 0
    return s

#Random set Initial solution
def Init_solution(num_object):
    packing = np.random.randint(0, 2, num_object)
    print("Random Initial Solution : ", packing)
    return packing

#計算packing的 total profits and total weights
def evaluate(packing):
    p = np.dot(packing, profits)
    w = np.dot(packing, weights)
    if w > capacity:
        p = 0
        return [p, w]
    else:
        return [p, w]  # returns total profits and total weights


def SimulatedAnnealing(iteration, initial_temperature ,Rt):
    '''
    current_sol -> 存放initial solution
    best_sol -> 存放最佳解，use copy() to not change when flip
    current_evl -> 存放目前solution的profits and weights值
    best_evl -> 計算best solution的profits and weights值
    temp -> use to checks the temperature, cooling scheduling(i) = temp(i)*0.95
    iterPro-> best total profits find in each iteration
    '''
    current_sol = Init_solution(num_object)
    best_sol = current_sol.copy()
    current_evl = evaluate(current_sol)
    best_evl = evaluate(best_sol)
    temp = initial_temperature

    iterPro = {}
    for i in range(iteration):
        #flip one position作為新的solution
        s = FlipOnePosition(current_sol)

        #當前的profit>先前的profit，update current solution
        if (evaluate(s)[0] > current_evl[0]):
            current_sol = s
            current_evl = evaluate(s)

        #退火環節
        else:
            delta = evaluate(s)[0] - current_evl[0]
            #隨機值 -> randomly set a float num between 0 and 1
            probability = random.uniform(0, 1)
            randomness = math.exp(delta / (temp))
            if (probability <= randomness):
                current_sol = s
                current_evl = evaluate(s)

        # Records the best value found so far
        if (current_evl[0] > best_evl[0]):
            best_sol = current_sol.copy()
            best_evl = current_evl

        #cooling scheduling
        temp *= Rt
        iterPro[i] = best_evl[0]

    print(iterPro)
    print(best_sol)
    p ,w = evaluate(best_sol)
    print("Best profit: ", p)
    print("Best weight: ", w)

    return iterPro

#output line chart
def plotOutput(sa_algo):
    plt.figure(figsize=(3.5, 3))
    plt.xticks(np.arange(0, iteration + 100, 100), fontsize=5)
    plt.yticks(np.arange(sa_algo[0], maxProfit, (maxProfit - sa_algo[0] + 1) / 8), fontsize=5)
    plt.plot(*zip(*sa_algo.items()))
    plt.xlabel('iteration', fontsize=7)
    plt.ylabel('optimal choice', fontsize=7)
    plt.title('Simulated Annealing ', fontsize=8)
    plt.show()

if __name__ == "__main__":
    #read input
    readFromFile()

    #if capacity == 0，print 0
    if capacity == 0:
        Solution = [0 for i in range(num_object)]
        print("optimal selection of weights = ", Solution)
        print("optimal selection of profits = ", 0)
    else:
        #先判斷所有object的weight總和是否大於capacity
        if checkMaxWeight() > capacity:
            # initial set
            iteration = 500
            initial_temperature = 5000
            Rt = 0.25
            #執行Simulated Annealing Algorithm
            sa_algo = SimulatedAnnealing(iteration, initial_temperature ,Rt)

            plotOutput(sa_algo)

        else:

            # total weights of every objects <=  capacity,
            Solution = [1 for i in range(num_object)]
            print("optimal selection of weights = ", Solution)
            print("optimal selection of profits = ", maxProfit)

