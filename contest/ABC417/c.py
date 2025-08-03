import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))

gap = []
sum = []
dict = {}
for i in range(n):
    gap.append(i+1 - a[i])
    sum.append(i+1 + a[i])
    dict[i+1-a[i]] = i+1
gap.sort()

ans = 0
for i in range(n):
    idx_l = bisect.bisect_left(gap, sum[i])
    idx_r = bisect.bisect_right(gap, sum[i])
    
    if idx_l < len(gap) and idx_r <= len(gap):
        if sum[i] == gap[idx_r-1]:
            '''
            while idx_l < idx_r: 
                if dict[gap[idx_l]] > i:
                    ans += 1
                idx_l +=1
            '''
            ans += idx_r - idx_l
        
    elif idx_l < len(gap)  :
        if sum[i] == gap[idx_l]: #and dict[gap[idx_l]] > i+1:
            ans += 1
            
print(ans)
