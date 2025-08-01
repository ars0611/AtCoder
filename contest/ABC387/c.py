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
l, r = map(int, input().split())

#rまでの蛇数の個数からl-1までの蛇数の個数を引けばよい
#さて、求め方がわからないうえに水diffなのでこの問題には緑になってからかえってこようと思います。