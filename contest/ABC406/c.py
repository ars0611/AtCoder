import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n = int(input())
p = list(map(int, input().split()))

r = []
for i in range(n - 1):
    if p[i] < p[i + 1]:
        r.append(1)
    else:
        r.append(0)

compresed_r = []
s = 0
g = 0
while g < n - 1:
    if r[s] == r[g]:
        g += 1
    else:
        compresed_r.append((r[s], g - s))
        s = g
compresed_r.append((r[s], g - s))

ans = 0
if len(compresed_r) >= 3:
    for i in range(len(compresed_r) - 2):
        if compresed_r[i][0] == 1 and compresed_r[i + 1][0] == 0 and compresed_r[i + 2][0] == 1:
            ans += compresed_r[i][1] * compresed_r[i + 2][1]

print(ans)
# 大小関係に関する情報をランレングス圧縮して配列で持っておく <- 思いつかんがな