import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import deque

#----------------------------------------#
# 入力
h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
a, b, c, d = map(int, input().split())
a -= 1; b -= 1; c -= 1; d -= 1 # 0-Indexですよ

cost = [[float("inf")] * w for _ in range(h)] # スタートから(i, j)に行くためのコスト
cost[a][b] = 0 # スタートは0
move = [(1,0), (0,1), (-1,0), (0, -1)] # 移動用
queue = deque([(a, b)]) # bfsします。
while queue:
    curi, curj = queue.popleft() # 現在の座標
    curc = cost[curi][curj] # 現在のコスト
    for k in range(4):
        ni = curi + move[k][0]
        nj = curj + move[k][1]
        if 0 <= ni < h and 0 <= nj < w:
            # 歩きの時
            if grid[ni][nj] == "." and cost[ni][nj] > curc:
                queue.appendleft((ni, nj))
                cost[ni][nj] = curc
            # 前蹴りするとき
            if grid[ni][nj] == "#":
                # 1マス進む用
                if cost[ni][nj] > curc + 1:
                    queue.append((ni, nj))
                    cost[ni][nj] = curc + 1
                # 2マス進む用
                nni = ni + move[k][0]
                nnj = nj + move[k][1]
                if 0 <= nni < h and 0 <= nnj < w and cost[nni][nnj] > curc + 1:
                    queue.append((nni, nnj))
                    cost[nni][nnj] = curc + 1
print(cost[c][d])

#01BFSなんか知らんよ。バイブルになかったもん（鉄則本）