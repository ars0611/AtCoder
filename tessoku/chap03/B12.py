import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict

#----------------------------------------#
n = int(input())

#にぶたんで間にあるようなxをもとめる
low = 0
high = 100
while low < high:
    mid = (low + high) / 2
    if abs(mid**3 + mid - n) <= 0.001:
        print(mid)
        exit()
    if mid ** 3 + mid > n:
        high = mid
    else:
        low = mid