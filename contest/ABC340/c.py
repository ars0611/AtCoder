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
nn = n
cnt = 0
while nn >= 2:
    nn //= 2
    cnt += 1
ans = 2**cnt * cnt + (n - 2**cnt)*(cnt + 2)
print(ans)