import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
#----------------------------------------#
# 引数について,0のときその面の総和を負を,1のとき正を目指す。
# 適宜正負を変えたのち,利益があるなら採用
def solve(front, back):
    s = 0
    for f, b in cards:
        if front == 0:
            f = -f
        if back == 0:
            b = -b
        if f + b >= 0:
            s += f + b
    return s

n = int(input())
cards = list(tuple(map(int, input().split())) for _ in range(n))

ans = 0
for i in range(2):
    for j in range(2):
        ans = max(ans, solve(i, j))

print(ans)