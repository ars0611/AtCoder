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
stack = []
for i in range(q):
    query = list(input().split())
    if query[0] == "1":
        x = query[1]
        stack.append(x)
    elif query[0] == "2":
        print(stack[-1])
    else:
        stack.pop()