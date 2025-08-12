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
#入力
x, y = map(int, input().split())

#x,yからさかのぼって1,1を目指す
ans = deque()
while x >= 1 and y >= 1:
    ans.appendleft([x, y])
    if x > y:
        x -= y
    else:
        y -= x

ans.popleft()
#出力
if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])