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
n = int(input())
r = input().strip()
c = input().strip()

l = ["A", "B", "C"] + ["."]*(n - 3)
rrow = defaultdict(set)
for line in itertools.permutations(l):
    f = ""
    i = 0
    while not f:
        if line[i] != ".":
            f = line[i]
        i += 1
    rrow[f].add(line)
row = dict()
for ch in "ABC":
    row[ch] = list(rrow[ch])

for grid in itertools.product(*(row[ch] for ch in r)):
    vert = [""]*n
    vert_cnt = [defaultdict(int) for _ in range(n)]
    for i in range(n):
        fst = ""
        for j in range(n):
            if grid[i][j] == ".": continue
            if not vert[j]:
                vert[j] = grid[i][j]
            vert_cnt[j][grid[i][j]] += 1
    if "".join(vert) == c and all(vert_cnt[j][ch] == 1 for j in range(n) for ch in "ABC"):
        print("Yes")
        for i in range(n):
            print("".join(grid[i]))
        exit()
print("No")