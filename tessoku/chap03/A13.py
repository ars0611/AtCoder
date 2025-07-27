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

#解説AC（しゃくとり法）


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