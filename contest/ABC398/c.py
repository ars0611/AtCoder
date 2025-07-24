import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)
dict_a = {}
for i,v in enumerate(a):
    dict_a[v] =i+1

if n == 1:
    print(a[i])
    exit()
ans_ai = -1
for i in range(n):
    if i == 0 and sorted_a[i] != sorted_a[i+1]:
        ans_ai = sorted_a[i]
    elif i == n-1 and sorted_a[i-1] != sorted_a[i]:
        ans_ai = sorted_a[i]
    elif sorted_a[i-1] != sorted_a[i] != sorted_a[i+1]:
        ans_ai = sorted_a[i]

if ans_ai == -1:
    print(-1)
else:
    print(dict_a[ans_ai])

#ごり押し