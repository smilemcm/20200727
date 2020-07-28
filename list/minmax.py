import sys

sys.stdin = open("minmax.txt","rt")
T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    #print(input_list.sort())
    sorted_input_list = sorted(input_list)
    min = sum(sorted_input_list[0:3])
    max = sum(sorted_input_list[-1:-4:-1])
    print("diff : ", max-min)