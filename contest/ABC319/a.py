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
rating = {"tourist":3858, "ksun48":3679, "Benq":3658, "Um_nik":3648, "apiad":3638, "Stonefeang":3630, "ecnerwala":3613, "mnbvmar":3555, "newbiedmy":3516, "semiexp":3481}
s = input().strip()
print(rating[s])