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
n = int(input())
a = list(map(int, input().split()))
b = []

#座標圧縮
sorted_a = sorted(list(set(a)))
dict_a = {}
for i in range(len(sorted_a)):
    dict_a[sorted_a[i]] = i+1

for i in range(n):
    b.append(dict_a[a[i]])

for i in range(n):
    print(b[i], end=" ")