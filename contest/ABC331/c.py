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
compresed_a = sorted(list(set(a)))
counter_a = Counter(a)
rank = dict()
diff = [0]
for i in range(len(compresed_a)):
    rank[compresed_a[i]] = i
    diff.append(diff[-1] + compresed_a[i] * counter_a[compresed_a[i]])
s = sum(a)

b = []
for i in range(n):
    b.append(s - diff[rank[a[i]] + 1])
print(*b)

# 一般的なデータ構造オールスター感謝祭