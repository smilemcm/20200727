import sys
import numpy as np

sys.stdin = open("list3.txt","rt")
T = int(input())

for t in range(T):

    n = int(input())
    number_list = list(map(str, input()))

    cnt_num = (int(max(number_list)) + 1)
    counts = [0] * cnt_num
    counts_acc = [0] * cnt_num

    for i in range(0, len(number_list)):
        counts[int(number_list[i])] +=1

    for i in range(0, len(counts)):
        counts_acc[i] = counts_acc[i-1] + counts[i]

    print(counts)
    print(counts_acc)

    result = [0] * len(number_list)

    for i in range(len(number_list)-1,-1, -1):
        counts_acc[int(number_list[i])] -= 1
        result[counts_acc[int(number_list[i])]] = number_list[i]

    print(np.argmax(counts))
    print(counts[np.argmax(counts)])
    print(result)
    #print(counts)
    print('##########################33')
