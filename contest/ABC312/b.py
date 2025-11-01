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
grid = [input().strip() for _ in range(n)]
TaKCode = ["###.?????", "###.?????", "###.?????", "....?????", "?????????", "?????....", "?????.###", "?????.###", "?????.###"]
for i in range(n - 8):
    for j in range(m - 8):
        cnt = 0
        for k in range(9):
            for l in range(9):
                if grid[i + k][j + l] == TaKCode[k][l]:
                    cnt += 1
        if cnt == 32:
            print(i + 1, j + 1)