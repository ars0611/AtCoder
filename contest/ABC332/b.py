import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
k, g, m = map(int, input().split())
water_in_glass = 0
water_in_cup = 0
for i in range(k):
    if water_in_glass == g:
        water_in_glass = 0
    elif water_in_cup == 0:
        water_in_cup = m
    else:
        if water_in_cup - (g - water_in_glass) >= 0:
            water_in_cup -= (g - water_in_glass)
            water_in_glass = g
        else:
            water_in_glass += water_in_cup
            water_in_cup = 0
print(water_in_glass, water_in_cup)