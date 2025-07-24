import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
def dfs(cur):
    seen[cur] =True
    for i in node[cur]:
        if seen[i] == False:
            dfs(i)

N,M = map(int, input().split())

if N != M:
    print("No")
    exit()
else:    
    node = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        node[a-1].append(b-1)
        node[b-1].append(a-1)
    
    for i in range(N):
        if len(node[i]) != 2:
            print("No")
            exit()

    seen =[False for _ in range(N)]
    dfs(0)

    if sum(seen) == N:
        print("Yes")
    else:
        print("No")