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
n = int(input())
s = input()

streak_a = 1
a = [0] * n
a[0] = 1
for i in range(len(s)):
    if s[i] == 'A':
        streak_a += 1
    else:
        streak_a = 1
    a[i+1] = streak_a

streak_b = 1
b = [0] * n
b[n-1] = 1
for i in range(len(s)-1, -1, -1):
    if s[i] == 'B':
        streak_b += 1
    else:
        streak_b =1
    b[i] = streak_b

ans = 0
for i in range(n):
    ans += max(a[i], b[i])
print(ans)