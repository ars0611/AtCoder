import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n, k = map(int, input().split())
sum = k
a = [1 for _ in range(n+1)]
for i in range(k,n+1):
    a[i] = sum
    sum -= a[i-k]
    sum += a[i]
    sum %= 10**9
print(a[n])

'''
和で管理
多分O(NK)でTLE
'''