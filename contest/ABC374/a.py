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
s = input()

if len(s) < 3:
    print("No")
    exit()

if s[-3:] == "san":
    print("Yes")
else:
    print("No")