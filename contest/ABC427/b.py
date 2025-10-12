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
def fa(num):
    cnt = 0
    while num > 0:
        cnt += num % 10
        num //= 10
    return cnt
n = int(input())
a = [1]
ans = 0
for i in range(n):
    ans += fa(a[i])
    a.append(ans)
print(ans)