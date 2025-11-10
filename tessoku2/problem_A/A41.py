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
n = int(input())
s = input().strip()

ans = False
for i in range(n - 2):
    if s[i] == s[i + 1] == s[i + 2]:
        ans = True

print("Yes" if ans else "No")

# 1マスずつずらして両サイドからマスを塗れば任意の色にできるので、白マス3マスを残して1マスずつ塗って良い
# 最後に余った3マスがsにおいて同色なら塗れるので,答えはYes
# つまり色が同一の3マスがあるかどうかで答えがわかる
# こんなんプログラミングじゃなくてクイズじゃん、僕には無理です。