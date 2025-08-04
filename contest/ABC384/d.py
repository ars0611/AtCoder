import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
n, s = map(int, input().split())
a = list(map(int, input().split()))

#累積和
sum_a = [0]*(n+1)
for i in range(1,n+1):
    sum_a[i] = sum_a[i-1] + a[i-1]

#s / sum_a[n]の商の数周するので、そのあまりをsとしaの部分列でつくれるか判定したい
s = s % sum_a[n]

#aの長さを二倍にした累積和に対して差がsになるものがあるか尺取り
for i in range(1,n+1):
    sum_a.append(sum_a[n]+sum_a[i])

r = 0
l = 0
sum = 0
comp = False
while r < 2*n+1:
    
    if r != 2*n and r == l:
        r += 1
    
    sum = sum_a[r] - sum_a[l]
    
    if sum == s:
        comp = True
        break

    elif sum < s:
        r += 1

    else:
        l += 1

if comp:
    print("Yes")
else:
    print("No")