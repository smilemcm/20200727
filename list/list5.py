import sys
import numpy as np

sys.stdin = open("list5.txt","rt")
T = int(input())
number_list =[  ]
matrix = []

total=0

for t in range(T):
    matrix = [[0] * 10 for i in range(10)]
    n = int(input())

    for _ in range(n):
        x1, y1, x2, y2, color = list(map(int, input().split()))

        for i in range(10):   #### line
            for j in range(10):  #### column
                if i >= x1 and j >= y1 and i <= x2 and j <= y2:
                    matrix[i][j] += 1


    for i in range(10):  #### line
        for j in range(10):  #### column
            if matrix[i][j] > 1:
                total += 1

    print(t, total)
    total = 0