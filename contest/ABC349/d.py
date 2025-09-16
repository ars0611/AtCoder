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
l, r = map(int, input().split())

p = [1] #2**iを前計算しとこうかな 
for i in range(61):
    p.append(p[-1] * 2)

ans = []
while l != r:
    i = 0
    while l + p[i] <= r and l % p[i] == 0:
        i += 1
    ans.append([l, l + p[i - 1]])
    l = l + p[i - 1]

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])

# なんだこの数学問題は。