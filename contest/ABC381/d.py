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

#尺取り
def syakutori(start):
    counter = Counter()
    l = r = start
    cnt = 0
    res = 0
    
    while l < n-1:
        
        #左端を決定
        if a[l] != a[l+1]:
            l += 2
            r = l
            cnt = 0
            counter.clear()
        
        #右端をずらす
        elif r < n-1 and a[r] == a[r+1] and counter[a[r]] == 0:
            counter[a[r]] += 1
            cnt += 2
            r += 2
            res = max(res, cnt)
        
        #左端をずらす
        else:
            counter[a[l]] -= 1
            l += 2
            cnt -= 2
            if l > r:
                r = l
        
    return res

ans = max(syakutori(0), syakutori(1))
print(ans)