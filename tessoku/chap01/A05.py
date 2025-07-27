N, K = map(int, input().split())
ans = 0
for i in range(N):
    for j in range(N):
        if 1 <= K - (i+1) - (j+1) <= N:
            ans += 1
print(ans)