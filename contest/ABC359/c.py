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
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

# スタートとゴールをタイルの左側に揃える
if (sx + sy) % 2 == 1:
    sx -= 1
if (tx + ty) % 2 == 1:
    tx -= 1

dx = abs(tx - sx)
dy = abs(ty - sy)
print(dy + max(dx, dy) // 2)

# 似た方針なのにWA数個取れなかったので泣く泣く解説AC