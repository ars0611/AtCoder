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
def Enumerate(list):
    sumList = []
    for i in range(1 << len(list)):
        s = 0
        for j in range(len(list)):
            if i & (1 << j):
                s += list[j]
        sumList.append(s)
    return sumList

n, k = map(int, input().split())
a = list(map(int, input().split()))

left = a[:n // 2]
right = a[n // 2:]
sum_left = sorted(Enumerate(left))
sum_right = sorted(Enumerate(right))

for i in range(len(sum_left)):
    num = k - sum_left[i]
    idx = bisect.bisect_left(sum_right, num)
    if idx < len(sum_right) and sum_right[idx] == num:
        print("Yes")
        break
else:
    print("No")