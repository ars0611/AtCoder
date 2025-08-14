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
n, c = input().split()
n = int(n)
a = list(input())

#どの手順でカードを減らしても同じ結果になる
#W = 0, B = 1, R = 2としたとき,操作について和を3で割ったあまりの数字のカードに変化することに着目する
score = 0
for i in range(n):
    if a[i] == "W":
        score += 0
    elif a[i] == "B":
        score += 1
    else:
        score += 2

score %= 3
if score == 0 and c == "W" or score == 1 and c == "B" or score == 2 and c == "R":
    print("Yes")
else:
    print("No")

#adhoc