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
n, m = map(int, input().split())
node = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b+1)
    node[b].append(a+1)

for i in range(n):
    output = ""
    output += str(i+1) + ": {"
    output += ", ".join(str(x) for x in node[i])
    output += "}"
    print(output)