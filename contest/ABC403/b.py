import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
T = input()
U = input()

for i in range(len(T)-len(U)+1):
    comp = True
    for j in range(len(U)):
        if not(T[i+j] == "?" or T[i+j] == U[j]):
            comp = False
            break
        if j == 3:
            comp =True
    if comp:
        print("Yes")
        exit()
if not comp:
    print("No")