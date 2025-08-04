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
a, b, c = map(int, input().split())
if a == b == c or a+b == c or a == b+c or a+c == b:
    print("Yes")
else:
    print("No")