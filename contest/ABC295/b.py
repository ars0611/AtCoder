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
r, c = map(int, input().split())
grid = list(list(input().strip()) for _ in range(r))
ans = [grid[i][:] for i in range(r)]
notBomb = set(["#", "."])

for i in range(r):
    for j in range(c):
        if grid[i][j] == ".": continue
        if grid[i][j] == "#":
            for k in range(r):
                for l in range(c):
                    if grid[k][l] in notBomb: continue
                    power = int(grid[k][l])
                    if abs(i - k) + abs(j - l) <= power:
                        ans[i][j] = "."
        else:
            ans[i][j] = "."

for i in range(r):
    print("".join(ans[i]))