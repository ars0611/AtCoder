import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
#----------------------------------------#
def dfs(cur, prev):
    if x[cur] != -1:
        return
    x[cur] = 1^prev
    for nxt in graph[cur]:
        if x[nxt] == -1:
            dfs(nxt, x[cur])
    return

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
graph = [[] for _ in range(n)]

x = [-1]*n
for i in range(m):
    ai = a[i] - 1
    bi = b[i] - 1
    graph[ai].append(bi)
    graph[bi].append(ai)

for i in range(n):
    if x[i] == -1:
        dfs(i, 1)

for i in range(m):
    if x[a[i] - 1] == x[b[i] - 1]:
        print("No")
        break
else:
    print("Yes")

# unionfindで親から0,1決めてけばもっと早い。