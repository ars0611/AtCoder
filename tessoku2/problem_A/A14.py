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
n, k = map(int, input().split())
a = list(map(int ,input().split()))
b = list(map(int ,input().split()))
c = list(map(int ,input().split()))
d = list(map(int ,input().split()))

sum1 =[]
sum2 = []
for i in range(n):
    for j in range(n):
        sum1.append(a[i] + b[j])
        sum2.append(c[i] + d[j])
sum1.sort()
sum2.sort()
ans = False
for i in range(n**2):
    idx = bisect.bisect_left(sum2, k - sum1[i])
    if idx < n ** 2 and sum2[idx] == k - sum1[i]:
        ans = True
        break
print("Yes" if ans else "No")