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
#10進数nをb進数変換する関数(2 <= b <= 10)
def base10_to_baseb(n,b):
    res = ""
    while n > 0:
        res = f'{n % b}' + res
        n //= b
    if res == "":
        return "0"
    else:
        return res
    
n = int(input())
tmp = base10_to_baseb(n-1, 5)
ans = 0
for i in range(len(tmp)):
    ans += int(tmp[i]) * 2
    if i != len(tmp) - 1:
        ans *= 10
print(ans)

# 確かに5進数