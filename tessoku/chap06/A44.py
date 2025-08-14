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
n, q = map(int, input().split())
a = list(range(1,n+1))

comp = False
for i in range(q):
    
    query_i = list(map(int, input().split()))
    
    if query_i[0] == 1:
        x = query_i[1]
        y = query_i[2]
        if comp:
            a[-x] = y
        else:
            a[x-1] = y
    
    elif query_i[0] == 2:
        if comp:
            comp = False
        else:
            comp = True

    else:
        x = query_i[1]
        if comp:
            print(a[-x])
        else:
            print(a[x-1])