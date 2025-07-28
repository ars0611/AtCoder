import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
#入力
n, k = map(int, input().split())
a = list(map(int, input().split()))

#ビット全探索でaのカードをいくつか選んだ合計を列挙
def Enumerate(list):
    sumlist= []
    for i in range(1 << len(list)):
        sum = 0
        for j in range(len(list)):
            if i >> j & 1:
                sum += list[j]
        sumlist.append(sum)
    return sumlist

#半分全列挙
left = a[0:n//2]
right = a[n//2:n]

#それぞれについて取りうる合計全列挙
sum_left = Enumerate(left)
sum_right = Enumerate(right)
sum_left.sort()
sum_right.sort()

#にぶたんでsum_left+sum_right = kとなるものが存在するか
for i in sum_left:
    idx = bisect.bisect_left(sum_right, k - i)
    if idx < len(sum_right) and sum_right[idx] == k - i:
        print("Yes")
        exit()
print("No")