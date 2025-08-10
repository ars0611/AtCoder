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

a = n // 100
b = (n-100*a)  // 10
c = n % 10

print(100*b + 10*c + a, 100*c + 10*a + b, end = " ")