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
n = int(input())
s = list(input())

#長さnの11/22文字列
t = ["1"]*(n // 2) + ["/"] + ["2"]*(n//2)

if s == t:
    print("Yes")
else:
    print("No")