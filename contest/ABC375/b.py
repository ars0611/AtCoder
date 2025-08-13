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

cost = 0
cur_x = 0
cur_y = 0
for i in range(n):
    x, y = map(int, input().split())
    cost += math.sqrt((x-cur_x)**2 + (y-cur_y)**2)
    cur_x = x
    cur_y = y
cost += math.sqrt(cur_x**2 + cur_y**2)

print(cost)