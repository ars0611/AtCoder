import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
score = list(map(int, input().split()))

rank = []
for i in range(1 << len(score)):
    sum = 0
    name = str()
    for j in range(len(score)):
        if i >> j & 1: 
            name += "ABCDE"[j]
            sum += score[j]
    rank.append([sum, name])

#第0列に着目して降順にsort
rank.sort(reverse = True)

#得点が同じrank[i]に対し、その範囲で第1列に着目して昇順にsort
first = 0
last = 0
for i in range(len(rank)):
    if (i-1 >= 0 or i == 0) and rank[i-1][0] != rank[i][0] and i+1 < 31 and rank[i][0] == rank[i+1][0]:
        first = i
        last = i+1
    elif i+1 < 31 and rank[i][0] == rank[i+1][0]:
        last += 1
    elif first != 0 and (i+1 < 31 or i == 30) and rank[i][0] != rank[i+1][0]:
        rank[first:last+1] =sorted(rank[first:last+1],key = lambda x:x[1])
        first = 0
        last = 0
for i in range(31):
    print(rank[i][1])

#先に名前順にsortすればどこからどこまでが同点か調べる必要がなかった。反省。