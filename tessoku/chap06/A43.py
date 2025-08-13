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
n, l = map(int, input().split())
a = []
b = []
for i in range(n):
    a_i, b_i = input().split()
    a_i = int(a_i)
    a.append(a_i)
    b.append(b_i)

#人を区別する必要がないので,ぶつかって方向転換することとすれ違うことを同一視する
#進む方向で場合分けして,出口から最も遠い人を全探索すればよい
ans = 0
for i in range(n):
    if b[i] == "W":
        time = a[i]
    else:
        time = l - a[i]
    ans = max(ans, time)

print(ans)