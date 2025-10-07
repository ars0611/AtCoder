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
s = input().strip()
t = input().strip()
sl = abs(ord(s[0]) - ord(s[1])) % 3
tl = abs(ord(t[0]) - ord(t[1])) % 3
if sl == tl or sl != 1 and tl != 1:
    print("Yes")
else:
    print("No")