import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect
import math
import itertools
import copy
from sortedcontainers import SortedSet, SortedList, SortedDict

#----------------------------------------#
q = int(input())
card = SortedSet()

for _ in range(q):
    query = list(input().split())
    if query[0] == "1":
        card.add(int(query[1]))
    elif query[0] == "2":
        card.remove(int(query[1]))
    elif query[0] == "3":
        if card:
            idx = card.bisect_left(int(query[1]))
            if idx < len(card):
                print(card[idx])
            else:
                print(-1)
        else:
            print(-1)