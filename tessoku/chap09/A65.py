import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
a = list(map(int, input().split())) 
node = [[] for _ in range(n)]
#部下から上司に辺を張る
#a[i]+1 := i+2の上司であることに注意
for i, a_i in enumerate(a):
    a_i -= 1
    i += 1
    node[a_i].append(i)

#部下の人数をdpで計算
#具体的には,葉から根に向かっていく形式
dp = [0]*n
for i in range(n-1, -1, -1):
    for j in node[i]:
        dp[i] += dp[j] + 1

print(*dp)