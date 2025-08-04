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
n, c_1, c_2 = map(str, input().split())
s = list(input())

for i in range(int(n)):
    if s[i] != c_1:
        s[i] = c_2
print("".join(s))