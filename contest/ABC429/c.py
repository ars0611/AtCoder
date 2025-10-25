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
l = len(a)
counter = Counter(a)
ans = 0
for num in counter.keys():
    if counter[num] >= 2:
        ans += (((counter[num]) * (counter[num] - 1)) // 2) * (l - counter[num])
print(ans)