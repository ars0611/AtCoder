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

a = [0]*n
a[0] = 1
a[1] = 1
for i in range(2,n):
    a[i] = (a[i-1] + a[i-2]) % (10**9 + 7)
print(a[n-1])