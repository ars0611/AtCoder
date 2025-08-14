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
q = int(input())
queue = deque()
for i in range(q):
    query = list(input().split())
    if query[0] == "1":
        x = query[1]
        queue.append(x)
    elif query[0] == "2":
        print(queue[0])
    else:
        queue.popleft()