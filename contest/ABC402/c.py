import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n, m = map(int, input().split())

dish = [] 
material = [[] for _ in range(n)] 

for i in range(m):
    dish.append(list(map(int, input().split())))

dislike = list(map(int, input().split()))

for i in range(m):
    for j in range(1,len(dish[i])):
        material[dish[i][j]-1].append(i+1)

ans = 0
for i in range(n):
    for j in material[dislike[i]-1]:
        dish[j-1][0] -= 1
        if dish[j-1][0] == 0:
            ans += 1
    print(ans)
