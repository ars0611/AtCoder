import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))

for i in range(n-1):
    if a[i] >= a[i+1]:
        print("No")
        exit()
print("Yes")