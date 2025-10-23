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
k = int(input())
good_nums = []
for bit in range(1 << 10):
    use = []
    for i in range(10):
        if bit & (1 << i):
            use.append(i)
    use.sort(reverse=True)
    good_num = 0
    for i in range(len(use)):
        good_num += use[i] * 10 ** (len(use) - i - 1)
    if good_num != 0:
        good_nums.append(good_num)
good_nums.sort()
print(good_nums[k - 1])