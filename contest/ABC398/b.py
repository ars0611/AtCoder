import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
a = list(map(int, input().split()))
a_num = list(set(a))
cnt_3 = 0
cnt_2 = 0
for i in a_num:
    if a.count(i) >= 3:
        cnt_3 += 1
    elif a.count(i) >= 2:
        cnt_2 +=1

if cnt_3 >= 2 or (cnt_3 >= 1 and cnt_2 >= 1):
    print("Yes")
else:
    print("No")