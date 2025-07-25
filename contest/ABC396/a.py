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
for i in range(n-2):
    if a[i] == a[i+1] == a[i+2]:
        print("Yes")
        exit()
print("No")