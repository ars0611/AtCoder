import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
#x秒でk枚以上印刷するか判定
def check(x, k, a):
    sum = 0
    for i in a:
        sum += x // i
    if sum >= k:
        return True
    return False

n, k = map(int,input().split())
a = list(map(int, input().split()))

l = 1
h = 10**9
while l<h:
    m = (l+h) // 2
    ans = check(m,k,a)
    if ans:
        h = m
    if not ans:
        l = m + 1
print(l)