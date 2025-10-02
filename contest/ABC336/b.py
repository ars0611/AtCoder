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
x = int(input())
x_base2 = format(x, 'b')
cnt = 0
i = 0
while i <= len(x_base2) and x_base2[-i-1] == "0":
    cnt += 1
    i += 1
print(cnt)