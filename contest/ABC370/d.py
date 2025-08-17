import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
h, w, q = map(int, input().split())
grid = [[0] * w for _ in range(h)]
ans = h*w
#q <= 2*10**5よりO(q)で解きたい
#壁に関する情報をうまく持つ方法があるのかな
#眠いので明日考える
for _ in range(q):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    grid[r][c] += 1

