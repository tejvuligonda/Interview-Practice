'''
Steve has a string, , consisting of  lowercase English alphabetic letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabcc" would become either "aab" or "bcc" after operation.

Steve wants to reduce  as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Steve out by finding and printing 's non-reducible form!

Note: If the final string is empty, print Empty String .

Input Format

A single string, s.

Constraints
n is from 1 to 100 inclusive

Output Format

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

Sample Input 0

aaabccddd
Sample Output 0

abd
Sample Case 0

Steve can perform the following sequence of operations to get the final string:

    aaabccddd -> abccddd
    abccddd -> abddd
    abddd -> abd
    Thus, we print abd.

    Sample Input 1

    baab
    Sample Output 1

    Empty String
    Explanation 1

    Steve can perform the following sequence of operations to get the final string:

    baab -> bb
    bb -> Empty String
    Thus, we print Empty String.

    Sample Input 2

    aa
    Sample Output 2

    Empty String
    Explanation 2

    Steve can perform the following sequence of operations to get the final string:

    aa -> Empty String
    Thus, we print Empty String.

Link: https://www.hackerrank.com/challenges/reduced-string
'''

import sys
if (sys.version_info > (3,0)):
    inp = input()
else:
    inp = raw_input()

def reduce(s):
    l = list(s)
    i = 0
    while i < (len(l)-1):
        if l[i] == l[i+1]:
            l.pop(i+1)
            l.pop(i)
            i = -1
        i+=1
    if (l):
        return ''.join(l)
    return 'Empty String'

if __name__ == "__main__":
    print(reduce(inp))
                                                                                                    
