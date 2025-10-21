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

score = [i + 1 for i in range(n)]
unsolved = [[] for _ in range(n)]
max_score = 0
for i in range(n):
    si = input().strip()
    for j in range(m):
        if si[j] == "o":
            score[i] += a[j]
        else:
            unsolved[i].append(a[j])
    max_score = max(max_score, score[i])

for i in range(n):
    need_score = max_score - score[i]
    unsolved[i].sort(reverse = True)
    cnt = 0
    while need_score > 0:
        need_score -= unsolved[i][cnt]
        cnt += 1
    print(cnt)