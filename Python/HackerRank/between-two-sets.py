#!/bin/python
'''
Consider two sets of positive integers, A  and B. We say that a positive integer, x, is between sets A  and B if the following conditions are satisfied:

All elements in A  are factors of x.
x is a factor of all elements in B.
Given A and B, find and print the number of integers (i.e., possible x's) that are between the two sets.

Input Format

The first line contains two space-separated integers describing the respective values of  (the number of elements in set ) and  (the number of elements in set ). 
The second line contains  distinct space-separated integers describing . 
The third line contains  distinct space-separated integers describing .

Constraints
1 <= n, m <= 100
1 <= element of a <= 100
1 <= element of b <= 100

Output Format
Print the number of integers that are considered to be between A  and B.

Sample Input
2 3
2 4
16 32 96

Sample Output
3

Explanation

The integers that are between   and  are , , and .

Link: https://www.hackerrank.com/challenges/between-two-sets
'''

import sys
from sets import Set

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

def getAllFactors(x):
    factors = set()
    for i in range(1,x+1):
        if x % i == 0:
            factors.add(i)
    return factors

def getInBetween(set1,set2):
    allIntegers = []
    for v in set2:
        allIntegers.append(getAllFactors(v)) # of each v and see what values are common between them
        valid = allIntegers[0]
        for s in allIntegers[1:]:
            valid.intersection_update(s)
    for w in set1:
        for integer in valid.copy():
            if integer % w != 0:
                valid.remove(integer)
    return len(valid)

print(getInBetween(a,b))
