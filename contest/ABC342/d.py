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
a = list(map(int, input().split()))
a.sort()
ans = a.count(0) * (len(a) - 1) - a.count(0) * (a.count(0) - 1) // 2
a = a[a.count(0):]
n = len(a)
is_square = []
is_not_square = []
for i in range(n):
    int_root_a = math.isqrt(a[i])
    if a[i] == int_root_a ** 2:
        is_square.append(a[i])
    else:
        tmp = a[i]
        num = 2
        while num < int_root_a + 1:
            if a[i] % num ** 2 == 0:
                tmp = a[i] // num ** 2
            num += 1
        is_not_square.append(tmp)

ans += len(is_square) * (len(is_square) - 1) // 2
counter = Counter(is_not_square)
for key in counter.keys():
    ans += counter[key] * (counter[key] - 1) // 2
print(ans)