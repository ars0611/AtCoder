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
m = int(input())
s = [list(input().strip()) * 3 for _ in range(3)]
ans = float("inf")
p = list(itertools.permutations([0, 1, 2]))
for reels in p: 
    for aim in range(10):
        aim = str(aim)
        sec = -1
        stopped = set()
        for reel in reels:
            for j in range(3 * m):
                if s[reel][j] == aim and j > sec:
                    stopped.add(reel)
                    sec = j
                    break
        if len(stopped) == 3:
            ans = min(ans, sec)

print(ans if ans != float("inf") else -1)

# reelを止める順も全探索しなければならない、俺はその順を列挙しきれてなかった