import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n = int(input())
s = []
for i in range(n + 1):
    for j in range(1, 10):
        if n % j == 0 and i % (n / j)== 0:
            s.append(str(j))
            break
    else:
        s.append("-")
print("".join(s))