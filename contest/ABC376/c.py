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
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()

cnt = 0
i = n-1
j = n-2
while i >= 0:
    if  j >= 0 and b[j] >= a[i]:
        j -= 1
        i -= 1
    else:
        cnt += 1
        ans = a[i]
        i -= 1

if cnt == 1:
    print(ans)
else:
    print(-1)