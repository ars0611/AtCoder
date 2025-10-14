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
n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(1, n + 1):
    for j in range(s + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
        else:
            if a[i - 1] > j: continue
            if dp[i - 1][j - a[i - 1]]:
                dp[i][j] = True

if dp[n][s]:
    ans = []
    cur_s = s
    cur_a = n
    while cur_s != 0 and cur_a != 0:
        if not dp[cur_a - 1][cur_s]:
            ans.append(cur_a)
            cur_s -= a[cur_a - 1]
        cur_a -= 1
    
    k = len(ans)
    ans.reverse()
    print(k)
    print(*ans)
else:
    print(-1)