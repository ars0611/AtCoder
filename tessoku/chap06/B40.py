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

dict_a = defaultdict(int)
for i in range(n):
    a[i] = a[i] % 100
    dict_a[a[i]] += 1

ans = 0
for i in range(51):
    if i == 0 or i == 50:
        ans += dict_a[i] * (dict_a[i] - 1) // 2
    else:
        ans += dict_a[i] * dict_a[100 - i]

print(ans)