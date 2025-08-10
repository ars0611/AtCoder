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
x = list(map(int, input().split()))
a = list(map(int, input().split()))

#xについてsort
b = []
for i in range(m):
    b.append([x[i],a[i]])
b.sort()

#累積和
sum = [0]*(m+1)
for i in range(1,m+1):
    sum[i] = sum[i-1] + b[i-1][1]

#石の総数はnでないと不可能
if sum[m] != n:
    print(-1)
    exit()

#マスiに必要な石数は合計i個
for i in range(1,m+1):
    if b[i-1][0]-1 > sum[i-1]:
        print(-1)
        exit()

#ここまで来れたら可能なので、操作回数を求める
s = 0
for i in range(m):
    s += b[i][0] * b[i][1]

print((n*(n+1)) // 2 - s)