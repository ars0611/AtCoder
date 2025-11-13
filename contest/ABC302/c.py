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
n, m = map(int, input().split())
l = [list(input().strip()) for _ in range(n)]

cmp = False
for ll in itertools.permutations(l):
    for i in range(n - 1):
        for j in range(m):
            if ll[i][:j] + ll[i][j + 1:] == ll[i + 1][:j] + ll[i + 1][j + 1:]:
                break
        else:
            break
        continue
    else:
        cmp = True

print("Yes" if cmp else "No")