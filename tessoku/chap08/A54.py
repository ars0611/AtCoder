import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
q = int(input())
score = {}
for _ in range(q):
    query = list(input().split())
    if query[0] == "1":
        x = query[1]
        y = int(query[2])
        score[x] = y
    else:
        x = query[1]
        print(score[x])