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
k = list(map(int, input().split()))

def Enumerate(list):
    s = sum(list)
    ans = 10**9
    for i in range(1 << len(list)):
        a = 0
        for j in range(len(list)):
            if i >> j & 1:
                a += list[j]
        b = s - a
        ans = min(ans, max(a,b))
    return ans

print(Enumerate(k))