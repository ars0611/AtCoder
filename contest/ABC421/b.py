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
x, y = map(int, input().split())
a = [str(x), str(y)]
for i in range(2, 10):
    a.append("")
    a_i = int(a[i-1]) + int(a[i-2])
    a_i = str(a_i)
    for j in range(-1, -len(a_i)-1, -1):
        if a_i[j] == "0" and a[i] == "":
            continue
        elif a[i] == "":
            a[i] = a_i[j]
        else:
            a[i] += a_i[j]
for i in range(10):
    a[i] = int(a[i])
print(a[9])
