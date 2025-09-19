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
l = len(s)

alphabets = [[] for _ in range(26)]
for i in range(l):
    alphabets[ord(s[i]) - ord("a")].append(i)

cmp = False
ans = l * (l - 1) // 2
for i in range(26):
    ll = len(alphabets[i])
    if ll:
        ans -= ll * (ll - 1) // 2
    if not cmp and ll >= 2:
        cmp = True

print(ans + 1 if cmp else ans)