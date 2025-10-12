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
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

def check(sec):
    cnt = 0
    for ai in a:
        if sec >= ai:
            cnt += sec // ai
        else:
            break
    return cnt

l = 1
r = 10**9
while l < r:
    m = (l + r) // 2
    tmp = check(m)
    if tmp < k:
        l = m + 1
    else:
        r = m

print(l)