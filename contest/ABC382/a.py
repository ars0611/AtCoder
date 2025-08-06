import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
import copy

#----------------------------------------#
n, d = map(int, input().split())
s = list(input())

cnt = s.count("@")
print(n-cnt+d)