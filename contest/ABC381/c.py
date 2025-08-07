import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
import copy

#----------------------------------------#
n = int(input())
s = list(input())

#sl_idx[i] := i+1文字目の/のidx
sl_idx = []
for i in range(n):
    if s[i] == "/":
        sl_idx.append(i)

ans = 0
for i in range(len(sl_idx)):
    idx = sl_idx[i]
    j = 1
    cnt = 0
    while 0 <= idx-j and idx+j <= n-1:
        if s[idx-j] == "1" and s[idx+j] == "2":
            cnt += 1
        else:
            break
        j += 1
    ans = max(ans, 2*cnt+1)

print(ans)