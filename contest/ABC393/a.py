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
s_1, s_2 = map(str, input().split())
if s_1 == s_2 == "sick":
    print(1)
elif s_1 =="sick" and s_2 == "fine":
    print(2)
elif s_1 == "fine" and s_2 == "sick":
    print(3)
else:
    print(4)