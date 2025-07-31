import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
a = list(map(int, input().split()))
sorted_a = sorted(a)

cnt = 0
for i in range(len(a)-1):
    if a[i] != sorted_a[i] and a[i+1] != sorted_a[i+1]:
        cnt += 1
if cnt == 1:
    print("Yes")
else:
    print("No")