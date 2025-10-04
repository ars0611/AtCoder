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
grid = [["#"]*(n + 2)]+ [(["#"] + ["0"]*n + ["#"]) for _ in range(n)] + [["#"]*(n + 2)]
grid[(n + 1) // 2][(n + 1) // 2] = "T"
p = 1
x = 1
y = 1
d = "r"
while p <= n** 2 - 1:
    grid[x][y] = f'{p}'
    if d == "r": 
        if grid[x + 1][y] == "0":
            x += 1
        else:
            d = "d"
            y += 1
    elif d == "d":
        if grid[x][y + 1] == "0":
            y += 1
        else:
            d = "l"
            x -= 1
    elif d == "l":
        if grid[x - 1][y] == "0":
            x -= 1
        else:
            d = "u"
            y -= 1
    else:
        if grid[x][y - 1] == "0":
            y -= 1
        else:
            d = "r"
            x += 1
    p += 1
for i in range(n):
    print(*grid[i + 1][1:n + 1])