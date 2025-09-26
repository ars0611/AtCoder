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
n, m, k = map(int, input().split())
g = math.gcd(n, m)
left = 0
right = 2 * 10**18
x = (n * m) // g
while left + 1 < right:
    mid = (left + right) // 2
    if mid // n + mid // m - 2 * (mid // x) >= k:
        right = mid
    else:
        left = mid

print(right)

# 包除原理を用いると, k以下の整数でn,m一方でのみで割れるものの個数は k//n + k//m - 2 * k//l
#  にぶたんでちょうどkを探す？