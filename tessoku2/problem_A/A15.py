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
a = list(map(int, input().split()))
ranked_a = sorted(list(set(a)))
rank = dict()
for i in range(len(ranked_a)):
    rank[ranked_a[i]] = i + 1
b = []
for i in range(n):
    b.append(rank[a[i]])
print(*b)