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
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

#半分全列挙
p = []
q = []
for i in range(n):
    for j in range(n):
        p.append(a[i]+b[j])
        q.append(c[i]+d[j])

q.sort()
#にぶたんでqにk-pが存在するか判定
for i in p:
    idx = bisect.bisect_left(q,k-i)
    if idx < n**2 and q[idx] == k-i:
        print("Yes")
        exit()
print("No")