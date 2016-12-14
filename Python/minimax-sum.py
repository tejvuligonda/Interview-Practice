'''Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

    A single line of five space-separated integers.

Constraints
    Each integer is in the inclusive range 1 to 10^9.

Output Format
    Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

Sample Input
    1 2 3 4 5

Sample Output
    10 14

Link: https://www.hackerrank.com/challenges/mini-max-sum
'''
#!/bin/python

import sys


#a,b,c,d,e = raw_input().strip().split(' ')
#a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

def minimaxsum(a,b,c,d,e):
    sorted_nums = sorted([a,b,c,d,e]) # O(n logn)
    min = sorted_nums[0] + sorted_nums[1] + sorted_nums[2] + sorted_nums[3]
    max = sorted_nums[1] + sorted_nums[2] + sorted_nums[3] + sorted_nums[4]
    result = str(min) + " " + str(max)
    print(result)
    
minimaxsum(1,2,3,4,5)
   

