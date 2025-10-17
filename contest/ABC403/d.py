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
n, d = map(int, input().split())
a = list((map(int, input().split())))
cnter = Counter(a)
ans = 0
if d == 0:
    ans = sum(v - 1 for v in cnter.values())
else:
    group = defaultdict(list)
    for v in cnter.keys():
        group[v % d].append(v)
    for key in group.keys():
        dp = [[0]*(len(group[key])) for _ in range(2)]
        group[key].sort()
        dp[0][0] = cnter[group[key][0]]
        for i, v in enumerate(group[key][1:]):
            if v - d == group[key][i]:
                dp[0][i + 1] = min(dp[0][i], dp[1][i]) + cnter[v]
                dp[1][i + 1] = dp[0][i]
            else:
                dp[0][i + 1] = min(dp[0][i], dp[1][i]) + cnter[v]
                dp[1][i + 1] = min(dp[0][i], dp[1][i])
        ans += min(dp[0][-1], dp[1][-1])
print(ans)
# ai mod d ごと削除数を求めて加算すればよい