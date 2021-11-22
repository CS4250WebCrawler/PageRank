import numpy as np
from fractions import Fraction as frac

# numbers here are based on lecture 8 Page Rank matrix example
# since there are 3 pages n = 3
n = 500 #for our crawler matrix
# n = 3 #for testing purposes

# importing the text file and turning it into a matrix of float data type
# m = np.loadtxt("testing.txt", dtype=float)
# m = np.loadtxt("CPP_Matrix.txt", dtype=float)
# since we will have two matrix from each web crawl
m = np.loadtxt("NPR_Matrix.txt", dtype=float)

# multiples m by the matrix and calculates the rank using random surfer model
def calcRank(matrix):
    # calculate iteration 1 without random surfer model
    basic_matrix = np.dot(m, matrix)
    # surfer is the lambda in the equation
    surfer = 0.2
    # multiply the basic page ranks in m1 by 1-lambda
    rank = np.dot(basic_matrix, (1 - surfer))
    # then add lambda/3 to each value in the matrix
    rank = rank + (surfer / n)
    return rank


def rankSum(matrix):
    # sum is still close to 1 after using random surfer model
    sum = 0
    for x in matrix:
        for y in x:
            sum += y
    return sum
    # print("\n sum after random surfer model: " + str(sum))


# creating the initial page rank (iteration 0)
# when we use 500 pages, we should make a loop that can create this array with 500 rows
m0 = []
for x in range(0, n):
    # print(x)
    m0.append([frac(1, n)])

prev_matrix = m0
new_matrix = calcRank(prev_matrix)

# convert matrices to string for easy comparison
while str(prev_matrix) != str(new_matrix):
    prev_matrix = new_matrix
    new_matrix = calcRank(prev_matrix)

# sum should be close to 1
print("sum: " + str(rankSum(new_matrix)))

# put the resulting page ranks in a text file
# openFile = open('CPP_Results', "w")
openFile = open('NPR_Results', "w")
for row in new_matrix:
    for num in row:
        openFile.write(str(num) + "\n")
