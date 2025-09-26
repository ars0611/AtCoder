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
n, w = map(int, input().split())

x = [[] for _  in range(w)] # 列ごとに積み上げて管理
for i in range(n):
    xi, yi = map(int, input().split())
    x[xi-1].append((yi, i))
m = n # 消えるのは列で一番低いとこの高さ分だけ
for i in range(w):
    x[i].sort()
    m = min(m, len(x[i]))

# i行目が何秒後に消えるか
h = [0]*m
for i in range(m):
    for j in range(w):
        h[i] = max(h[i], x[j][i][0])

block = [float("inf")] * n
for i in range(len(h)):
    for j in range(w):
        block[x[j][i][1]] = h[i]

q = int(input())
for _ in range(q):
    t, a = map(int, input().split())
    a -= 1
    print("Yes" if t < block[a] else "No")

# 座圧ちっくに考えた。もうちょいきれいにコード書けた気もするが、リファクタはいいや