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

t = "abcdefghijklmnopqrstuvwxyz"
q = int(input())
for _ in range(q):
    c, d = input().split()
    t = t.replace(c, d)

ans = ""
for i in range(n):
    ans += t[ord(s[i]) - ord("a")]
print(ans)