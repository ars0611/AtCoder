import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
d = int(input())

#aについて先頭からと末尾からとで累積MAXをとる
p = [None]*n
q = [None]*n
p[0] = a[0]
q[0] = a[n-1]
for i in range(1,n):
    p[i] = max(a[i], p[i-1])
    q[i] = max(a[n-1-i], q[i-1])


for _ in range(d):
    l, r = map(int, input().split())
    print(max(p[l-2], q[n-r-1]))