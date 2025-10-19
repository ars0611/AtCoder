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
s = input()
for i in range(n- 1):
    if s[i] + s[i + 1] == "ab" or s[i] + s[i + 1] =="ba":
        print("Yes")
        break
else:
    print("No")