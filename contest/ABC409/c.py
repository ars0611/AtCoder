import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque, Counter
import bisect

#----------------------------------------#
n, l = map(int, input().split())
d = list(map(int, input().split()))

if l % 3 != 0:
    print(0)
    exit()

s = [0]
for i in range(n-1):
    s.append((s[-1] + d[i]) % l)
c = Counter()
for si in s:
    c[si] += 1

ans = 0
for i in range(l // 3):
    ans += c[i] * c[i + l // 3] * c[i + l // 3 * 2]

print(ans)