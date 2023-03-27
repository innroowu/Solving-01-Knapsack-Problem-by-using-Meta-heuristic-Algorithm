# Solving 01 Knapsack Problem by using Meta-heuristic Algorithm
This project uses the Hill Climbing Algorithm and Simulated Annealing Algorithm to solve the 01 Knapsack Problem.

The datasets used in this project is from：
https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html

### **Format of Input File (P07 as example)：**  
```
750       							（the knapsack capacity）  
70,73,77,80,82,87,90,94,98,106,110,113,115,118,120     		（the weights of the object）  
135,139,149,150,156,163,173,184,192,201,210,214,221,229,240    	（the profits of each objects）  
1,0,1,0,1,0,1,1,1,0,0,0,0,1,1     				（the optimal selection of weights）   
```

**! Please note that you will need to change the file been used in the code to wherever you have stored the dataset.**  
**! Also, you should set your input file format as above (Format of Input File)**

## **Hill Climbing Algorithm**   
Hill Climbing Algorithm is a meta-heuristic iterative local search algorithm. It can be useful in a variety of optimization problems. It starts with an initial solution and then iteratively makes small changes to it in order to improve the solution. 

### **How**  
1.	Input the number of Iteration.
2.	Randomly generate a initial solution and set it as the best solution
(Notice：Because it is randomly selected, it is possible that the initial solution be the optimal solution, or the total profit of initial solution is 0) 
3.	Calculate the total profit of the best solution
4.	Randomly pick a position from the best solution, and update the position’s value from 1 to 0 or 0 to 1 
5.	Calculate the total profit of the solution after updating the position
6.	If the total profit of the solution is better than the original solution, update the best solution, if not, maintain the original solution
7.	Continue iteration, repeat flow 3 to 5
8.	Find the Best solution, and make a line chart according to the number of iteration and the best solution found in each iteration


## **Simulated Annealing Algorithm**    
Simulated annealing is a probabilistic variation of Hill Climbing that allows the algorithm to occasionally accept worse moves in order to avoid getting stuck in local maxima.

### **How**
1.	Randomly generate a initial solution and set it as the best solution.
2.	Define a sufficiently large value as the initial temperature.
3.	Flip one position of the previous solution from 1 to 0 or 0 to 1 as a new solution.
4.	If new solution’s fitness value is better than previous solution, then update it.
5.	If is not, perform Annealing. The solution is then updated if it matches the formula.
### $$r≤exp(Δf/T)$$
>Delta f (Δf) = Difference between the fitness values of current and new solution  
>Random num (r) = random float number between 0-1  
>T = temperature  
6.	If it’s better than best solution ,than update it.
7.	Whether it is updated or not, the cooling action must be performed at the end of the iteration.  
### $$T=T×Rₜ$$
>T = temperature
>Rₜ = depends on the desired convergence speed
8.	Execute the next iterations at the new temperature state
9.	Make a line chart according to the number of iteration and the best solution found in each iteration

