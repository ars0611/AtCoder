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
n, a, b= map(int, input().split())
s= input().strip()

cnt_a = [0]
cnt_b = [0]
for ch in s:
    if ch == "a":
        cnt_a.append(cnt_a[-1] + 1)
        cnt_b.append(cnt_b[-1])
    else:
        cnt_a.append(cnt_a[-1])
        cnt_b.append(cnt_b[-1] + 1)

ans = 0
for left in range(1, n + 1):
    idx_a = bisect.bisect_left(cnt_a, a + cnt_a[left - 1])
    idx_b = bisect.bisect_left(cnt_b, b + cnt_b[left - 1])
    if idx_b < idx_a: continue
    ans += idx_b - idx_a

print(ans)

# 尺取り、別に左端を全探索からの右端を二分探索で良い感じにできる説