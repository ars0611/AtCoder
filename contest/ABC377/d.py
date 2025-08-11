import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
#入力
n, m = map(int, input().split())

#d[r] := rを終点とした際の条件を満たすlの値
d = [1 for _ in range(m+1)]
for i in range(n):
    l, r = map(int, input().split())
    d[r] = max(d[r], l + 1)

for r in range(1,m+1):
    d[r] = max(d[r], d[r-1])

ans = 0
for r in range(1,m+1):
    ans += r - d[r] + 1

print(ans)

#尺取りかるに考える。
#各l,rに関してその始点と終点に着目してしまっていたからうまくいかなかった。