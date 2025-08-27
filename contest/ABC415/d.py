import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
#----------------------------------------#
# 入力
# 必要瓶数と交換レートで受け取る
n, m = map(int, input().split())
exc = []
for _ in range(m):
    a_i, b_i = map(int, input().split())
    exc.append((a_i, a_i - b_i))

exc.sort(key=lambda x: x[1]) # 交換レートについてsort
cur = n # 手持ちの瓶数
ans = 0 # 手持ちのシール数
# 小さい順に見ていく
for i in range(m):
    if cur >= exc[i][0]:
        ans += max((math.ceil(cur - exc[i][0])) // exc[i][1] + 1, 0) # できるかぎり交換
        cur -= max(((math.ceil(cur - exc[i][0])) // exc[i][1] + 1) * exc[i][1], 0) # 交換した回数分瓶を減らす
print(ans)