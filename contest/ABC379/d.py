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
q = int(input())
p = deque()
t = 0
cnt = 0
for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        p.append(-t)
    
    elif query[0] == 2:
        t += query[1]

    else:
        ans = 0
        while len(p) != 0:
            if query[1] - t <= p[0]:
                ans += 1
                p.popleft()
            else:
                break
        print(ans)