import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict

#----------------------------------------#
n, k = map(int, input().split())
a = list(map(int, input().split()))

#解法２解説AC（しゃくとり法）
R = [0]*n
for i in range(n):
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i-1]

    while R[i] < n-1 and a[R[i] + 1] - a[i] <= k:
        R[i] += 1

ans = 0
for i in range(n):
    ans += (R[i]-i)
print(ans)
#自力AC解法１（にぶたん）
'''
cnt = 0
for i in range(n):
    idx = bisect.bisect_left(a, a[i] + k)
    if idx < n and a[idx] == a[i] + k:
        cnt += idx - i
    else:
        cnt += idx - i - 1
print(cnt)
'''