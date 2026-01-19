import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
from functools import lru_cache
#----------------------------------------#
class BIT:
    def __init__(self, N):
        self.N = N
        self.bits = [0] * (self.N + 1)
        
    def update(self, i, x):
        while i <= self.N:
            self.bits[i] += x
            i += i & -i
    
    def total(self, i):
        res = 0
        
        while i > 0:
            res += self.bits[i]
            i -= i & -i
            
        return res

n = int(input())
s = input().strip()
preS = [0]
for ch in s:
    if ch == "A":
        preS.append(preS[-1] - 1)
    elif ch == "B":
        preS.append(preS[-1] + 1)
    else:
        preS.append(preS[-1])
val = sorted(set(preS))
idx = {v:i + 1 for i, v in enumerate(val)}
bit = BIT(len(val))
ans = 0
for i in range(n, -1, -1):
    ans += bit.total(idx[preS[i]] - 1)
    bit.update(idx[preS[i]], 1)
print(ans)
