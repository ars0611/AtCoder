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
pres = [0]
sufs = [0]
if k % 2 == 0:
    ans = 0
    for i in range(0, k, 2):
        ans += a[i + 1] - a[i]
else:
    pres = [0] # 先頭からペアをつくったときの累積和
    sufs = [0] # 末尾からペアを作った時の累積和
    for i in range(0, k - 1, 2):
        pres.append(pres[-1] + a[i + 1] - a[i])
    for i in range(k - 1, 1, -2):
        sufs.append(sufs[-1] + a[i] - a[i - 1])
    sufs.reverse()
    ans = float("inf")
    for i in range(len(sufs)):
        ans = min(ans, sufs[i] + pres[i])
print(ans)
# お隣同士をペアにすればうまくいきそうなのは、直観的にそうだった。
# 選ばないやつを決めたとき,ペアが一個ずれるせいでこの問題は難しくなってる
# 末尾からの累積和を取っておくことで解決 <-天才か？？
# 数列の長さが奇数だし言われてみればそうですが、自分じゃ思いつきません
# バグらせてうざいので明日実装しなおす