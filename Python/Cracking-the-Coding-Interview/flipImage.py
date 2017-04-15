#!/usr/bin/python3
# Page 73 of Cracking the Coding Interview
# 1.6 Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

import pprint

def flipImage(img):
    result = [[None for x in range(len(img))] for y in range(len(img))]
    k = len(img)
    for i in range(len(img)):
        k-=1
        for j in range(len(img)):
            print(i,j)
            result[len(img)-1-j][k] = img[i][j]
    return result

inp33 = [[1,2,3],[4,5,6],[7,8,9]]
inp44 = [[1,2,3],[4,5,6],[7,8,9]]

print(flipImage(inp33))
