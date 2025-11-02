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
n = int(input())
x = list(map(int, input().split()))

line = SortedList()
line.add(0)
res = 0
for i in range(n):
    if i == 0:
        res += x[i] * 2
    else:
        idx = line.bisect_left(x[i])
        if idx < len(line):
            res += min(abs(line[idx] - x[i]), abs(x[i] - line[idx - 1]))
        else:
            res += x[i] - line[-1]
        if idx == len(line):
            res -= line[-1] - line[-2]
            res += min(abs(x[i] - line[idx - 1]), abs(line[idx - 1] - line[idx - 2]))
        else:
            if idx + 1 != len(line):
                res -= (min(abs(line[idx + 1] - line[idx]), abs(line[idx] - line[idx - 1])))
                res += min(abs(line[idx] - x[i]), abs(line[idx + 1] - line[idx]))
            else:
                res -= line[-1] - line[-2]
                res += line[-1] - x[i]
            res -= min(abs(line[idx] - line[idx - 1]), abs(line[idx - 1] - line[idx - 2]))
            res += min(abs(x[i] - line[idx - 1]), abs(line[idx - 1] - line[idx - 2]))
        
        
    line.add(x[i])
    print(res)