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
n, m = map(int, input().split())

#同じ頂点に向かう/逆向きにしただけ/重複する 辺を消すのでそれを数え上げる
path = set()
ans = 0
for i in range(m):
    u,v = map(int, input().split())
    if u == v:
        ans += 1
    elif (v,u) in path:
        ans += 1
    elif (u,v) in path:
        ans += 1
    else:
        path.add((u,v))
print(ans)