# エラトステネスの篩によるn以下の素数の列挙
n = int(input())
dp = [True] * (n - 1)       # dp[i] := i + 2が素数かどうかをboolで持つ
for i in range(n - 1):      # 素数の倍数は合成数であることを利用して配るDPのイメージ
    if not dp[i]: continue
    dp[i] = True
    num = (i + 2) * 2
    while num <= n:
        dp[num - 2] = False
        num += i + 2