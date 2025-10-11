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
a = list(map(int, input().split()))
score = defaultdict(int)
winner = -1
for i in range(m):
    score[a[i]] += 1
    if score[a[i]] > score[winner]:
        winner = a[i]
    elif score[a[i]] == score[winner]:
        winner = min(winner, a[i])
    print(winner)