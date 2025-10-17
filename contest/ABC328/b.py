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
def is_same(num):
    s = set()
    while num > 0:
        s.add(num % 10)
        num //= 10
    if len(s) == 1:
        res = s.pop()
    else:
        res = 0
    return res

n = int(input())
d = list(map(int, input().split()))
ans = 0
for i in range(n):
    num = is_same(i + 1)
    if num:
        while num <= d[i]:
            ans += 1
            num = num * 10 + num
print(ans)