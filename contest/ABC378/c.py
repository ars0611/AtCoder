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
a = list(map(int, input().split()))

dict_a = defaultdict(int)
b = []
for i in range(n):
    idx = dict_a[a[i]]
    if idx == 0:
        b.append(-1)
    else:
        b.append(idx)
    dict_a[a[i]] = i+1

print(*b)