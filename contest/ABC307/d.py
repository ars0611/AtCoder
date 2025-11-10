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

stack_brkt = []
stack_idx = []
brkt = set(["(", ")"])
todel = []
for i in range(n):
    if s[i] not in brkt: continue
    
    if stack_brkt and  stack_brkt[-1] == "(" and s[i] == ")":
        stack_brkt.pop()
        start = stack_idx.pop()
        end = i
        if not todel:
            todel.append((start, end))
        else:
            while todel:
                prev_start, prev_end = todel[-1]
                if start <= prev_start and prev_end <= end:
                    todel.pop()
                else:
                    break
            todel.append((start, end))
    
    else:
        stack_brkt.append(s[i])
        stack_idx.append(i)

isdeled = [False]*n
for start, end in todel:
    for i in range(start, end + 1):
        isdeled[i] = True

ans = []
for i in range(n):
    if not isdeled[i]:
        ans.append(s[i])

print("".join(ans))