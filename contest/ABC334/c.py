import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n, k = map(int, input().split())
a = list(map(int, input().split()))

# お隣同士をペアにすればうまくいきそうなのは、直観的にそうだった。
# 選ばないやつを決めたとき,ペアが一個ずれるせいでこの問題は難しくなってる
# 末尾からの累積和を取っておくことで解決 <-天才か？？
# 数列の長さが奇数だし言われてみればそうですが、自分じゃ思いつきません
# バグらせてうざいので明日実装しなおす