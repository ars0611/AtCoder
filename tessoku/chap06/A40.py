import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))

a.sort()
i = 0
j = 0
cnt = 1
p = []
while i < n-2 and j < n:
    
    if a[i] != a[i+1]:
        i += 1
        j = i
    
    elif j < n-1 and a[j] == a[j+1]:
        cnt += 1
        j += 1

    elif j == n-1 or a[j] != a[j+1]:
        if cnt >= 3:
            p.append(cnt)
        cnt = 1
        i = j + 1
        j = i

ans = 0
for num in p:
    ans += num * (num - 1) * (num - 2) // 6 # 3つ選ぶ組み合わせ
print(ans)