import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
s = list(input())
t = list(input())
x = []

if s == t:
    print(0)

else:
    swap_order = []
    for i in range(len(s)):
        if ord(s[i]) > ord(t[i]):
            swap_order.append(i)
    for idx in swap_order:
        s[idx] = t[idx]
        x.append("".join(s))
    i = -1
    while s != t:
        if s[i] != t[i]:
            s[i] = t[i]
            x.append("".join(s))
        i -= 1

    print(len(x))
    for x_i in x:
        print(x_i)