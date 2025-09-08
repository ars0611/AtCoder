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
i = int(s[0]); j = int(s[2])
if j < 8:
    print(f'{i}-{j+1}')
if i < 8 and j == 8:
    print(f'{i+1}-1')
