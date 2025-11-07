import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
#----------------------------------------#
def get_idx(i, ans):
    a, b = res[i]
    left = 0
    right = len(ans)
    while left < right:
        mid = (left + right) // 2
        if res[ans[mid]][0] * (a + b) < a * (res[ans[mid]][0] + res[ans[mid]][1]):
            left = mid + 1
        else:
            right = mid
    return left

n = int(input())
res = []
for i in range(n):
    a, b = map(int, input().split())
    res.append((a, b))

ans = []
for i in range(n - 1, -1, -1):
    idx = get_idx(i, ans)
    ans.insert(idx, i)
    
ans = [ans[i] + 1 for i in range(n - 1, -1, -1)]
print(*ans)

# 添え字で二分探索
# 昇順を作って、同じ確率の人は左挿入。最後に逆順取得でok
# cmp_to_key関数でsortする際の関数を決められるらしい