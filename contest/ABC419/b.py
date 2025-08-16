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
q = int(input())
box  = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        box.append(query[1])
    else:
        ans = 101
        for i in range(len(box)):
            if box[i] < ans:
                idx = i
                ans = box[i]
        print(ans)
        box.pop(idx)