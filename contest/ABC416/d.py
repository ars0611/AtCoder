import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    a.reverse()
    cnt = 0
    i = 0
    j = 0
    while i < n and j < n:
        if a[i] + b[j] < m:
            j += 1
        else:
            cnt += 1
            i += 1
            j += 1
    print(sum(a) + sum(b) - cnt * m)

#a_i + b_i >= m をできるだけ多く作る貪欲で答えが求まるのは考察できてた。
# 尺取り法頭になさすぎた