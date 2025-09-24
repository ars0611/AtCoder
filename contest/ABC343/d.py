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
n, t = map(int, input().split())
score = [0]*n
score_counter = Counter(score)
ans = set([0])
for _ in range(t):
    ai, bi = map(int, input().split())
    ai -= 1
    score_counter[score[ai]] -= 1
    if score_counter[score[ai]] == 0:
        ans.discard(score[ai])
    score[ai] += bi
    score_counter[score[ai]] += 1
    ans.add(score[ai])
    print(len(ans))