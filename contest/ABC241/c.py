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
from functools import lru_cache
from functools import cmp_to_key
#----------------------------------------#
n = int(input())
s = [input().strip() for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(n):
    for j in range(n):
        x, y = i, j
        for k in range(8):
            cnt = 0 if s[x][y] == '#' else 1
            curx, cury = x, y 
            for l in range(5):
                curx += dx[k]
                cury += dy[k]
                if not (0 <= curx < n and 0 <= cury < n): break
                if s[curx][cury] == '.':
                    cnt += 1
            else:
                if cnt <= 2:
                    print("Yes")
                    exit()
print("No")
