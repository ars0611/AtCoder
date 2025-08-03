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
a,b,c,d = map(int, input().split())
l = list(set([a,b,c,d]))
if len(l) == 2:
    print("Yes")
else:
    print("No")