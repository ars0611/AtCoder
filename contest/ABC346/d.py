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
s = input().strip()
c = list(map(int, input().split()))

#10...10 + 01.. or 01...01 + 10.. or 01...010 + 01... or 10...101 + 10...
c10 = [0]
c01 = [0]
for i in range(n):
    if i % 2 == 0 and s[i] == "1" or i % 2 == 1 and s[i] == "0":
        c01.append(c01[-1] + c[i])
        c10.append(c10[-1])
    else:
        c10.append(c10[-1] + c[i])
        c01.append(c01[-1])

ans = float('inf')
for i in range(n - 1):
    cand = min(c01[i + 1] + c10[n] - c10[i + 1], c10[i + 1] + c01[n] - c01[i + 1])
    ans = min(ans, cand)
print(ans)

# 良い文字列は限られてるからそれを普通に作るだけ。
# ABC422Cと似てる