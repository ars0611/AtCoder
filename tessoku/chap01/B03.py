import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#######################################回答########################################
n = int(input())
price = sorted(list(map(int, input().split())))
for i in range(n-2):
    for j in range(i+1,n-1):
        if 1000 - price[i] - price[j] in price[j+1:n]:
            print("Yes")
            exit()
print("No")