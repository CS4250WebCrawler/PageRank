import numpy as np
from fractions import Fraction as frac

#read matrix from our crawler code to calc page rank
data = np.loadtxt("crawler.txt", skiprows=1, dtype='str')
print(data)

# how to make matrices using numpy
m1 = np.array([[0.5,0.5,0],
               [0.5,0,1],
               [0,0.5,0]])
# using frac right now but ideally we won't need it, just have to import the numbers from crawler's matrix
m2 = np.array([[frac(1,3)],
               [0.5],
               [frac(1,6)]])
# m3 is the basic page rank (not using random surfer model)
m3 = np.dot(m1,m2)
print(m3)
# m1, m2, and m3 are based on the lecture ex and the answer is correct

# check that sum of page ranks = 1
sum = 0
for x in m3:
    for y in x:
        sum += y
print(sum)

# surfer is the lambda in the equation
surfer = 0.2
# since there are 3 pages n = 3
n = 3
# multiply the basic page ranks in m3 by 1-lambda
mult = np.dot(m3,(1-surfer))
print(mult)
# then add lambda/3 to each
rank = mult + (surfer/n)

# sum is still 1 after using random surfer model
sum = 0
for x in rank:
    for y in x:
        sum += y
print(sum)

# need to loop the matrix multiplication and random surfer model until the previous calculated rank is the same
# as the newly calculated rank. here's an example of how to check if two matrices are the same
an_array = np.array([[1,2],[3,4]])
another_array = np.array([[1,2],[3,4]])

comparison = an_array == another_array
equal_arrays = comparison.all()
# true, they are the same
print(equal_arrays)