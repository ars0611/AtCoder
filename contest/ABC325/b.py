import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict

#----------------------------------------#
n = int(input())
#key := 時差, value := 参加可能人数の合計
dict = defaultdict(int)
for i in range(n):
    w, x = map(int, input().split())
    dict[x] += w

ans = 0
for i in range(24):
    sum = 0
    for j in range(9):
        sum += dict[(i+j)%24]
    ans = max(ans,sum)
print(ans)

#提出後に思ったが、普通にiを時差とする長さ24の配列でよかったな