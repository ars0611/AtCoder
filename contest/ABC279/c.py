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
h, w = map(int, input().split())
s = [input().strip() for _ in range(h)]
t = [input().strip() for _ in range(h)]
colS = []
colT = defaultdict(int)
for j in range(w):
    colSi = []
    colTi = []
    for i in range(h):
        colSi.append(s[i][j])
        colTi.append(t[i][j])
    colS.append("".join(colSi))
    colT["".join(colTi)] += 1
for col in colS:
    if colT[col] == 0:
        print("No")
        break
    colT[col] -= 1
else:
    print("Yes")
