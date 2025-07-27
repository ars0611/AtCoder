import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
#回答

D = int(input())
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

B = [0]*(D+2) #B[i]にi-1日目からの参加者の増減を格納
ans = [0]*(D+2) #ans[i]にi日目の出席者を格納

for i in range(N):
    B[A[i][0]] += 1
    B[A[i][1]+1] -= 1

for i in range(1,D+1):
    ans[i] = ans[i-1] + B[i]
    print(ans[i])
