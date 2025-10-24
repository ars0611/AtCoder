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
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
pos = defaultdict(tuple)
pos[0] = (0, 0)
q = deque()
seen = set()
for _ in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, x, y))
    graph[b].append((a, -x, -y))
    if a == 0 and a not in seen:
        q.append(a)
        seen.add(a)
    if b == 0 and b not in seen:
        q.append(b)
        seen.add(b)
while q:
    cur_person = q.popleft()
    cur_x, cur_y = pos[cur_person]
    for nxt_person, diff_x, diff_y in graph[cur_person]:
        pos[nxt_person] = (cur_x + diff_x, cur_y + diff_y)
        if not nxt_person in seen:
            q.append(nxt_person)
            seen.add(nxt_person)

for i in range(n):
    if pos[i]:
        print(pos[i][0], pos[i][1])
    else:
        print("undecidable")