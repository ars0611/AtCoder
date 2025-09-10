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
a = sorted(list(map(int, input().split())))
cnt = 0 # 10**8を超える組(ai,aj)の数
for i in range(n):
    if a[i] >= 10**8 // 2:
        cnt += n-1-i
        continue
    idx = bisect.bisect_left(a, 10**8 - a[i])
    cnt += n - idx

print((n-1) * sum(a) - 10**8*cnt)

# modは引き算に言い換えられる。%でくくりたかったら引き算で考える