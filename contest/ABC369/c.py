import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
if n ==1:
    print(1)
    exit()

else:
    l = 0
    r = l+1
    d = a[r] - a[l]
    #長さ1の等差数列の分は先に数えておく
    ans = 0

    while r < n:
        
        if r < n-1 and a[r+1] - a[r] == d:
            r += 1
            
        else:
            ans += (r-l+1)*(r-l+2)//2 -1
            l = r
            r = l + 1
            if r < n-1:
                d = a[r] - a[l]

    print(ans+1)