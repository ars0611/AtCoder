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
n, h, w = map(int, input().split())
a = []
b = []
for i in range(n):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)

#一つの駒に対し、左に動ける回数の山と上に動ける回数の山があると考えるとニムれる
xor_sum = (a[0]-1) ^ (b[0]-1)
for i in range(1,n):
    xor_sum = xor_sum ^ (a[i]-1) ^ (b[i]-1) 

if xor_sum != 0:
    print("First")
else:
    print("Second")