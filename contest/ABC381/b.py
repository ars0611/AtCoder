import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
import copy

#----------------------------------------#
s = input()

str_set = set()
comp = True
if len(s) % 2 == 1:
    comp=False

for i in range(len(s)-1):
    if i % 2 == 0 and (s[i] != s[i+1] or s[i] in str_set) :
        comp = False 
    str_set.add(s[i])

if comp:
    print("Yes")
else:
    print("No")