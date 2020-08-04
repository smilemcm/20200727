import sys
import numpy as np

sys.stdin = open("list6.txt","rt")
T = int(input())
number_list =[  ]
matrix = []

total=0

for t in range(T):
    k, s = list(map(int, input()))


    