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
grid = []
for _ in range(3):
    c1, c2, c3 = map(int, input().split())
    grid += [c1, c2, c3]

ok = 0
order = list(itertools.permutations(list(range(9))))
for p in order:
    rows = [[] for _ in range(3)]
    cols = [[] for _ in range(3)]
    dia = [[] for _ in range(3)]
    
    for idx in p:
        num = grid[idx]
        rows[idx // 3].append(num)
        cols[idx % 3].append(num)
        if idx == 0 or idx == 4 or idx == 8:
            dia[0].append(num)
        if idx == 2 or idx == 4 or idx == 6:
            dia[1].append(num)
    
    comp = True
    for i in range(3):
        if rows[i][0] == rows[i][1] and rows[i][2] != rows[i][0]:
            comp = False
        if cols[i][0] == cols[i][1] and cols[i][2] != cols[i][0]:
            comp = False
    for i in range(2):
        if dia[i][0] == dia[i][1] and dia[i][2] != dia[i][0]:
            comp = False
    if comp:
        ok += 1

print(ok / len(order))