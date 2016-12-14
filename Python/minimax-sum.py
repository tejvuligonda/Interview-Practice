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

def minimaxsum_nlogn(a,b,c,d,e):
    sorted_nums = sorted([a,b,c,d,e]) # O(n logn)
    min_sum = sorted_nums[0] + sorted_nums[1] + sorted_nums[2] + sorted_nums[3]
    max_sum = sorted_nums[1] + sorted_nums[2] + sorted_nums[3] + sorted_nums[4]
    result = str(min_sum) + " " + str(max_sum)
    print(result)
   
def minimaxsum(a,b,c,d,e):
    nums        = [a,b,c,d,e]
    smallindex  = 0
    bigindex    = 0
    min_sum     = 0
    max_sum     = 0
    for i in range(0,5): # iterates from 0 to 4 inclusive
        if (nums[i]) < nums[smallindex]:
            smallindex = i
        if (nums[i]) > nums[bigindex]:
            bigindex = i
    for j in range(0,5):
        if j != bigindex:
            min_sum += nums[j]
        if j != smallindex:
            max_sum += nums[j]
    result = str(min_sum) + " " + str(max_sum)
    print(result)
    return result


if __name__ == "__main__":
    minimaxsum(1,2,3,4,5) # 10 14
    minimaxsum(10,10,10,10,9) # 39 40
 

