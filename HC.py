import numpy as np
import random
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

    #optimal_select -> the optimal selection of weights
    #maxProfits -> 在optimal selection下的最大profit總和
    #num_object -> 總共有多少個object
    global optimal_select,num_object,maxProfit
    maxProfit = 0
    optimal_select = [int(os) for os in inputFile.readline().split(",")]
    maxProfit = np.dot(optimal_select,profits)
    #print(maxProfit)
    num_object = len(optimal_select)
    inputFile.close()

#計算所有object的weight總和
def checkMaxWeight():
    MaxWeight = 0
    for i in range(len(weights)):
        MaxWeight += weights[i]

    return MaxWeight

#計算目前所取的object的profit總和
def calculate_profit(choosen, capacity, profits, weights):
    nowProfit = 0
    nowWeight = np.dot(choosen,weights)
    if nowWeight <= capacity:
        nowProfit = np.dot(choosen,profits)

    return nowProfit

#random挑選一個object的position，將其從 0變1 or 1變0
def FlipOnePosition(bc,num_object):
    position = random.randint(0, num_object - 1)
    if bc[position] == 0:
        bc[position] = 1
    else:
        bc[position] = 0
    return bc

#Hill Climbing Algo
def HillClimbing(iter_num, capacity, profits, weights, num_object):
    iterPro = {}

    #randomly set a initial solution
    packing = np.random.randint(0, 2, num_object)
    #best_profit -> 用來儲存最佳解的profit值
    best_profit = calculate_profit(packing, capacity, profits, weights)
    #BestPacking -> 儲存最佳解
    BestPacking = packing.copy()

    print("Initial Solution = ", packing)

    #進行500次迭代
    for i in range(iter_num):
        print("\nIteration ",i+1," : ")

        # choose -> 根據前一個解隨機產生一組解
        packing = FlipOnePosition(packing, num_object)
        print("Random solution = ",packing)
        pack_profit = calculate_profit(packing, capacity, profits, weights)

        #隨機產生的一組解之profit，如果profit值大於目前最佳解的profit值，則將其設為目前最佳解
        if pack_profit >= best_profit:
            best_profit = pack_profit
            BestPacking = packing.copy()

        #best total profits find in each iteration
        iterPro[i] = best_profit
        print("Best packing      = ",BestPacking,", profit = " , best_profit)

    return iterPro

#output line chart
def plotOutput(hc_algo):
    plt.figure(figsize=(3.5, 3))
    plt.xticks(np.arange(0, Iteration + 100, 100), fontsize=5)
    #plot的y軸，輸出6個
    plt.yticks(np.arange(hc_algo[0], maxProfit, (maxProfit - hc_algo[0] + 1) / 6), fontsize=5)
    plt.plot(*zip(*hc_algo.items()))
    plt.xlabel('iteration', fontsize=7)
    plt.ylabel('optimal choice', fontsize=7)
    plt.title('Hill Climbing Algo ', fontsize=8)
    plt.show()

if __name__ == "__main__":
    #先讀取input
    readFromFile()
    '''print("MaxProfit = ",maxProfit)'''

    #如果capacity == 0，直接print出全部的
    if capacity == 0:
        Solution = [0 for i in range(num_object)]
        print("optimal selection of weights = ",Solution)
        print("optimal selection of profits = ", 0)
    else:
        #先判斷所有object的weight總和是否大於capacity
        if checkMaxWeight() > capacity:
                #可輸入需要迭代?次
                #Iteration = int(input("Iteration: "))
                Iteration = 500

                #執行Hill CLimbing Algo
                hc_algo = HillClimbing(Iteration, capacity, profits, weights, num_object)
                '''print(hc_algo)'''

                plotOutput(hc_algo)

        else:
            # 所有object的weight總和 <=  capacity
            Solution = [1 for i in range(num_object)]
            print("optimal selection of weights = ", Solution)
            print("optimal selection of profits = ", maxProfit)



