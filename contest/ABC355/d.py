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
l = []
r = []
for _ in range(n):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)
l.sort()
r.sort()
j = 0
ans = n * (n-1) // 2
for i in range(n):
    while r[j] < l[i]:
        j += 1
    ans -= j
print(ans)

# 余事象を考える <- 確かに愚直に区間の重なりを数えるのはしんどい
# 区間が重ならないのは r_j < l_i を満たす組(i, j)
# l_i < r_i は常に成り立つので、l,rはsortしてよい
# rを昇順に見ていく <- 区間を扱う問題の典型
# sort以外のところはO(n)