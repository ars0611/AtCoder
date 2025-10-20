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
s = input().strip()
c = Counter(s)

s_int = [int(s[i]) for i in range(n)]
s_int.sort(reverse=True)
max_num = 0
for i in range(n):
    max_num += s_int[i]
    if i != n - 1:
        max_num *= 10

max_sq = math.isqrt(max_num)
sq_nums = list()
for i in range(max_sq + 1):
    sq_nums.append(str(i*i))

ans = 0
for sq_num in sq_nums:
    d = len(sq_num)
    if n - d > c["0"]: continue
    for ch in sq_num:
        if ch != "0" and c[ch] != sq_num.count(ch) or ch == "0" and c[ch] != n - d + sq_num.count(ch):
            break
    else:
        ans += 1
print(ans)