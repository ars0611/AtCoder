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
n = int(input())
movie = []
for i in range(n):
    l, r = map(int, input().split())
    movie.append([l, r])

movie.sort(key=lambda x: x[1])
cur = 0
i = 0
ans = 0
while cur < 86400 and i < n: #制約より時間の最大値は86400

    if i <= n-1 and movie[i][0] >= cur:
        ans += 1
        cur = movie[i][1]
    
    i += 1
print(ans)