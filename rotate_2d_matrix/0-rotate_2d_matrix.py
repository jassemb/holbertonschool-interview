#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    N = len(matrix)
    for x in range(0,int(N/2)):
        for y in range(x,N-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][N-1-x]
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
            matrix[N-1-y][x] = temp
def printing(matrix):
    for i in range(0,N):
        for j in range(0,N):
            print(matrix[i][j] , end = ' ')
            print("")
