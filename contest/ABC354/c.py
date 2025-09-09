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
cards = []
for i in range(n):
    a, c = map(int, input().split())
    cards.append((a, c, i+1))
cards.sort(reverse = True)

ans = []
cost = cards[0][1]
for i in range(n):
    if cards[i][1] > cost:
        continue
    ans.append(cards[i][2])
    cost = cards[i][1]

ans.sort()
print(len(ans))
print(*ans)