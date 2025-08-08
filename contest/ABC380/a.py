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
n = input()
if n.count("1") == 1 and n.count("2") == 2 and n.count("3") == 3:
    print("Yes")
else:
    print("No")