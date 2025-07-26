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

n, k, x =map(int,input().split())
s = []
for _ in range(n):
    s_i = input()
    s.append(s_i)

l = [i for i in range(n)]
a = []
for v in itertools.product(l,repeat=k):
    a.append(list(v))

f_a = []
for i in range(n**k):
    for j in range(k):
        if j == 0:
            w = s[a[i][j]]
        else:
            w += s[a[i][j]]
    f_a.append(w)

f_a.sort()
print(f_a[x-1])

#コンテスト中視野狭まっててupsolveになってしまった...