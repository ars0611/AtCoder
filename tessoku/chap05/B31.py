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
n = int(input())

a1 = n // 3 + n // 5 + n // 7
a2 = n // 15 + n // 21 + n // 35
a3 = n // 105

ans = a1 - a2 + a3
print(ans)