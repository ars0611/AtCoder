# LT紹介用問題
# https://atcoder.jp/contests/abc330/tasks/abc330_a

n, l = map(int, input().split())    # 入力
a = list(map(int, input().split())) # 入力
cnt = 0                             # 合格人数
for i in range(n):                  # i = 0, 1, ..., n-1
    if a[i] >= l:                   # 人iが合格ならば
        cnt += 1                    # 合格人数に1足す
print(cnt)                          # 答えを出力 

