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
priority_queue = []
heapq.heapify(priority_queue)
for i in range(q):
    query = list(input().split())
    
    if query[0] == "1":
        x = int(query[1])
        heapq.heappush(priority_queue, x)
    elif query[0] == "2":
        ans = heapq.heappop(priority_queue)
        print(ans)
        heapq.heappush(priority_queue, ans)
    else:
        heapq.heappop(priority_queue)