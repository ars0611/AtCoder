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
d = input()
direction = ["N", "E", "W","S", "NE", "NW", "SE", "SW"]
opposition =["S", "W", "E","N", "SW", "SE", "NW", "NE"]
for i in range(8):
    if d == direction[i]:
        print(opposition[i])