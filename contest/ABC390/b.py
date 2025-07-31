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

if n == 2:
    print("Yes")
    exit()


for i in range(n-2):
    if a[i+1]**2 != a[i]*a[i+2]:
        print("No")
        exit()
print("Yes")