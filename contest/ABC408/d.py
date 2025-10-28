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
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    zero = [0]                      # i文字目までの0の個数の累積和
    one = [0]                       # i文字目までの1の個数の累積和
    diff = [0]                      # zero_i - one_i
    cnt = 0
    for ch in s:
        if ch == "1":
            one.append(one[-1] + 1)
            zero.append(zero[-1])
            cnt += 1
        else:
            one.append(one[-1])
            zero.append(zero[-1] + 1)
        diff.append(zero[-1] - one[-1])
    
    res = 0
    m = 0
    for i in range(1, n + 1):
        res = min(res, diff[i] - m)
        m = max(m, diff[i])

    print(res + cnt)

# なんか要復習かも