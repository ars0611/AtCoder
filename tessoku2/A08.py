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
# 入力
h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

s = [[0]*(w+1) for _ in range(h+1)] # 累積和用のgrid

# 横方向の累積和
for i in range(h):
    for j in range(w):
        s[i+1][j+1] += s[i+1][j] + grid[i][j]

# 縦方向の累積和
for j in range(w):
    for i in range(h):
        s[i+1][j+1] += s[i][j+1]

# 出力
q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(s[c][d] - s[a-1][d] - s[c][b-1] + s[a-1][b-1])