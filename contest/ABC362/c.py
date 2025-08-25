import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n = int(input())
l = []
r = []
ans = []
for _ in range(n):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)
    ans.append((ri - li) // 2 + li)
cnt = sum(ans)
i = 0
while cnt != 0 and i < n:
    if cnt < 0:
        if cnt + r[i] - ans[i] < 0:
            cnt += r[i] - ans[i]
            ans[i] = r[i]
        else:
            ans[i] -= cnt
            cnt = 0
    else:
        if cnt - (ans[i] - l[i]) > 0:
            cnt -= (ans[i] - l[i])
            ans[i] = l[i]
        else:
            ans[i] -= cnt
            cnt = 0
    i += 1
if cnt != 0:
    print("No")
else:
    print("Yes")
    print(*ans)