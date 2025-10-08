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
s = input().strip()

total_t = 0
logo_t = 0
cnt_total_t= 0
cnt_logo_t = 0
for ch in s:
    if ch == "0":
        total_t = max(cnt_total_t, total_t)
        logo_t = max(cnt_logo_t, logo_t)
        cnt_total_t = 0
        cnt_logo_t = 0
    elif ch == "1":
        cnt_total_t += 1
    else:
        cnt_total_t += 1
        cnt_logo_t += 1
total_t = max(cnt_total_t, total_t)
logo_t = max(cnt_logo_t, logo_t)

if total_t > m:
    ans = max(total_t - m, logo_t)
else:
    ans = logo_t

print(ans)