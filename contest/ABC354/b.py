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
user = []
t = 0
for _ in range(n):
    s, c = input().split()
    t += int(c)
    user.append((s,int(c)))
user.sort()
winner = t % n
print(user[winner][0])