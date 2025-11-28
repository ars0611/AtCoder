import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
#----------------------------------------#
# seg = SegTree(初期の配列, 操作, 初期値)
class SegTree:
    """
        * init_val: 初期化用の配列
        * segfunc:  区間の操作
        * ide_ele:  単位元（配列の初期値）
        * n:        要素数
        * num:      n以上の最小の2のべき乗
        * tree:     セグメント木(1-index)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele]* 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
    
    """
    * k番目の値をxに更新
    * k: index(0-index)
    * x: 更新する値
    """
    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1
    
    """
    * [l, r)にsegfuncしたものを得る
    * l: index(0-index)
    * r: index(0-index)
    """
    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
# todo
ide_ele = 10**18
def segfunc(a, b):
    return(min(a, b))

n, l, r = map(int, input().split())
x = list(map(int, input().split()))
seg = SegTree([ide_ele]*n, segfunc, ide_ele)
seg.update(0, 0)
for i in range(1, n):
    left = bisect.bisect_left(x, x[i] - r)
    right = bisect.bisect_right(x, x[i] - l)
    seg.update(i, seg.query(left, right) + 1)
print(seg.query(n - 1, n))

# 貰うDPで貰ってこれる区間の最小を得ればその地点について解けるので、セグ木で高速化