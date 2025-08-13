import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
n, m = map(int, input().split())
a = list(map(int, input().split()))

#AC数に着目するとa_iに対し,n-1人分各要素加算しなければならないので,WA数に着目する。
wa = [0]*n
for i in range(m):
    wa[a[i]-1] += 1

for i in range(n):
    print(m - wa[i])