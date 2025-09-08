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
h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            cnt = 0
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] == "#":
                    cnt += 1
            if cnt != 2 and cnt != 4:
                print("No")
                exit()
print("Yes")