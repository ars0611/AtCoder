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
dice= []
side = []
for _ in range(n):
    k, *a = map(int, input().split())
    dice.append(Counter(a))
    side.append(k)
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        prob = 0
        for k in dice[i].keys():
            prob += dice[i][k] / side[i] * dice[j][k] / side[j]
        ans = max(ans, prob)
print(ans)