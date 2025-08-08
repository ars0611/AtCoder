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

xor_sum = a[0]
for i in range(1,n):
    xor_sum = xor_sum ^ a[i]

if xor_sum >= 1:
    print("First")
else:
    print("Second")