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
l = list(map(int, input().split()))
l_space = [l[i] + 1 for i in range(n)]

def solve(width):
    cnt = 1
    cur = -1
    for i in range(n):
        if cur + l_space[i] <= width:
            cur += l_space[i]
        else:
            cnt += 1
            cur = -1 + l_space[i]
    if cnt <= m:
        return True
    else:
        return False

left = max(l_space) - 1
right = sum(l_space) - 1
while left < right:
    mid = (left + right) // 2
    if solve(mid):
        right = mid
    else:
        left = mid + 1
print(left)