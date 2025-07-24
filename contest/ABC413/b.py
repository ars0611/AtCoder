import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N = int(input())
S = list(input() for i in range(N))
ans = []

for i in range(N-1):
    for j in range(i+1,N):
        compA = True
        compB = True
        if ans == []:
            ans.append(S[i] + S[j])
            if ans[0] != S[j] + S[i]:
                ans.append(S[j] + S[i])
        else:
            for k in range(len(ans)):
                if ans[k] == S[i] + S[j]:
                    compA = False        
                if S[i] + S[j] == S[j] + S[i] or ans[k] == S[j] + S[i]:
                    compB = False            
            if compA:
                ans.append(S[i] + S[j])
            if compB:
                ans.append(S[j] + S[i])
print(len(ans))
#センス、無し