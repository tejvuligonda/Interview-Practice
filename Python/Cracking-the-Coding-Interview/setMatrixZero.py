#!/usr/bin/python3
# Page 73 of Cracking the Coding Interview
# 1.7  Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0

import numpy as np

def setZeroCoord(matrix, coordinates):
    for i in range(len(coordinates)):
        row = coordinates[i][0]
        for j in range(len(matrix[row])):
            matrix[row][j] = 0
        col = coordinates[i][1]
        for j in range(len(matrix)):
            matrix[j][col] = 0
        #print(row,col)
        #matrix[row][col] = 0
    return matrix

def getZeros(matrix):
    coords = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 0):
                coords.append((i,j))
    return setZeroCoord(matrix,coords)

if __name__ == '__main__':
    inp1 = [[]]
    inp2 = [[0,1,1,1],[0,0,1,1]]
    inputs = [inp1,inp2]
    for i in inputs:
        print('input:')
        print(np.matrix(i))
        print('output:')
        print(np.matrix(getZeros(i)))
