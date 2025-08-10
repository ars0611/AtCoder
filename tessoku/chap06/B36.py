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
n, k = map(int, input().split())
s = input()

if s.count("1") % 2 == k % 2:
    print("Yes")
else:
    print("No")