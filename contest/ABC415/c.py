import sys
sys.setrecursionlimit(10**6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
t = int(input())
for _ in range(t):
    
    #入力
    n = int(input())
    s = input()
    
    #状態0は安全
    s = "0" + s
    dp = [False] * (len(s))
    dp[0] = True
    
    #各状態からいける状態を探索
    for i in range(len(s)):
        
        #危険な状態はスキップ
        if dp[i] == False:
            continue
        
        for j in range(n):
            
            if i & (1 << j) == "1":
                continue

            if s[i | (1 << j)] == "0":
                dp[i | (1 << j)] = True

    print("Yes" if dp[-1] else "No")