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
line = defaultdict(int)
dup = 0
for i in range(m):
    a, b = map(int, input().split())
    line[(a + b) % n] += 1
ans = m * (m + 1) // 2
for key in line.keys():
    k = line[key]
    ans -= k * (k + 1) // 2
print(ans)

# a - bで傾き分類しようとしてうまくいかなかった。
# (a + b) mod n で分類なのか、惜しい