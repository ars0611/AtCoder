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
s = input()

p = []
for i, s_i in enumerate(s):
    if s_i == "t":
        p.append(i)

ans = 0
for i in range(len(p)-1):
    for j in range(i + 1, len(p)):
        if p[j] - p[i] + 1 >= 3:
            ans = max((s[p[i]:p[j]+1].count("t")-2)/ (p[j]-p[i]+1 -2), ans)

print(ans)