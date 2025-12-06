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
#----------------------------------------#
n = int(input())
s = list(input().strip())
ans = []
i = 0
while i < n:
    if s[i:i + 2] == ["n", "a"]:
        ans.append("nya")
        i += 2
    else:
        ans.append(s[i])
        i += 1
print("".join(ans))
