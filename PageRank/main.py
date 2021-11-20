import numpy as np
from fractions import Fraction as frac

# numbers here are based on lecture 8 Page Rank matrix example
# since there are 3 pages n = 3
# n = 500 #for our crawler matrix
n = 3
# importing the text file and turning it into a matrix of float data type
m = np.loadtxt("matrix.txt", dtype=float)


# since we will have two matrix from each web crawl
# m2=np.loadtxt("matrix2.txt", dtype=float)

# Initializing pagerank value in the node class, not sure if needed
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.auth = 1.0
        self.hub = 1.0
        self.pagerank = 1.0


# creating the initial page rank (iteration 0)
# when we use 500 pages, we should make a loop that can create this array with 500 rows
for x in range(0, 500):
    m0 = np.array([[frac(1, n)],
                   [frac(1, n)],
                   [frac(1, n)]])
    # i named it m1 cuz this is the result for iteration 1
    m1 = np.dot(m, m0)
    # the result for the first iteration, is the same as his slide 11
    print(m1)
    break

# check that sum of page ranks = (or close to) 1
sum = 0
for x in m1:
    for y in x:
        sum += y
print("\n sum: " + str(sum))

# surfer is the lambda in the equation
surfer = 0.2
# multiply the basic page ranks in m1 by 1-lambda
rank = np.dot(m1, (1 - surfer))
# then add lambda/3 to each
rank = rank + (surfer / n)

print("\nmatrix after 1 iteration using random surfer model: \n" + str(rank))

# sum is still close to 1 after using random surfer model
sum = 0
for x in rank:
    for y in x:
        sum += y
print("\n sum after random surfer model: " + str(sum))

# iteration 2 would just be multiplying m by the rank from iteration 1 (slide 12)
print("\n Iteration 2: ")
# then m times rank from iteration 2, and so on until the previous rank is the same as the newly calculated rank
# here's an example of how to check if two matrices are the same
an_array = np.array([[1, 2], [3, 4]])
another_array = np.array([[1, 2], [3, 4]])
comparison = an_array == another_array
equal_arrays = comparison.all()
# true, they are the same
print("\nIs the matrices both the same: ")
print(equal_arrays)
