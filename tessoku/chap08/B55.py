import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
q = int(input())
card = SortedSet()
for i in range(q):
    query = list(input().split())
    if query[0] == "1":
        card.add(int(query[1]))
    else:
        if card:
            x = int(query[1])
            idx = card.bisect_left(x)
            if idx < len(card):
                m = min(abs(x - card[idx]), abs(x - card[idx - 1]))
            else:
                m = abs(x - card[idx - 1])
            print(m)
        else:
            print(-1)

#なんかline27,29でerrorlensが訴えかけてきてるけど普通に実行できる。なんやこいつ。無視しよ無視無視