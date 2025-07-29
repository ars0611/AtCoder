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
for i in range(len(a)):
    if a[(i+2) % 3] == a[(i+1) % 3] * a[i % 3]:
        print("Yes")
        exit()
print("No")