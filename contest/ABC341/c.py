import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
h, w, n = map(int, input().split())
t = input().strip()
grid = [list(input().strip()) for _ in range(h)]
dx = t.count("R") - t.count("L")
dy = t.count("D") - t.count("U")

def move(y, x, cnt):
    if cnt == len(t):
        return True

    if t[cnt] == "L":
        ny = y
        nx = x - 1
    elif t[cnt] == "R":
        ny = y
        nx = x + 1
    elif t[cnt] == "U":
        ny = y - 1
        nx = x
    elif t[cnt] == "D":
        ny = y + 1
        nx = x

    if grid[ny][nx] == ".":
        return move(ny, nx, cnt + 1)
    else:
        return False

ans = set()
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if grid[i][j] == ".":
            if move(i, j, 0):
                ans.add((i + dy, j + dx))

print(len(ans))
