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
s = input().strip()
visited = set([(0, 0)])
move = {"L":(1, 0), "R":(-1, 0), "U":(0, 1), "D":(0, -1)}
pos = (0, 0)
for ch in s:
    pos = (pos[0] + move[ch][0], pos[1] + move[ch][1])
    if pos in visited:
        print("Yes")
        break
    visited.add(pos)
else:
    print("No")
