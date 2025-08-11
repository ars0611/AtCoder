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
n,m = map(int, input().split())

cnt = 0
dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
visited = set()
for i in range(m):
    
    a,b = map(int, input().split())
    if (a, b) not in visited:
        cnt += 1
        visited.add((a, b))
    
    for j in range(8):
        nx = a + dx[j]
        ny = b + dy[j]
        if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in visited:
            visited.add((nx, ny))
            cnt += 1

print(n*n - cnt)