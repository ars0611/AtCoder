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
n, m = map(int, input().split())
c = list(map(int, input().split()))
zoo = [[] for _ in range(n)]
for i in range(m):
    k, *z = map(int, input().split())
    for zz in z:
        zoo[zz - 1].append(i)

ans = float("inf")
for bit in range(1 << n):
    cnt =  [0]*m
    cst = 0
    for i in range(n):
        if bit & (1 << i):
            cst += c[i]
            for j in range(len(zoo[i])):
                cnt[zoo[i][j]] += 1
    cnt_min = min(cnt)
    if cnt_min >= 2:
        ans = min(ans, cst)
    elif min(cnt) >= 1:
        for bbit in range(1 << n):
            ncnt = cnt[:]
            ncst = cst
            for ii in range(n):
                if bbit & (1 << ii):
                    ncst += c[ii]
                    for k in range(len(zoo[ii])):
                        ncnt[zoo[ii][k]] += 1
            if min(ncnt) >= 2:
                ans = min(ans, ncst)
print(ans)
# bit全探索で動物園を各動物園0~2回訪れることパターンを列挙すると2**(2*n)
# コードが汚すぎて明らかに非想定
# 3進数でのbit全炭治郎も最初に検討したが、普通に実装方法思いつかなかったわ
# bitシフトのところを//と%でうまいことやって,0,1,2に応じてコストさ加算するだけっぽいので簡単そう