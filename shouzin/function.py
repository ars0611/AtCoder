# 直積
# 長さnで各要素が一つ前の要素の10以上大きい数の組み合わせを全列挙する
# ただし、最後の要素の上限はm
# 直積を抽象化したライブラリ思いつかないからしばらくこれを書き換えて頑張る
n, m = map(int, input().split())
ans = []

def solve(v):
    size = len(v)
    if size == n:
        ans.append(v.copy())
        return
    if size == 0:
        start = 1
    else:
        start = v[-1] + 10
    limit  = m - 10*(n - size - 1)
    for i in range(start, limit + 1):
        v.append(i)
        solve(v)
        v.pop()
solve([])

# 深さ優先探索(dfs) curをrootとし、通ったnodeをTrueとする。
# True数がnodeの個数と一致するとき、nodeは連結である。
def dfs(cur):
    seen[cur] =True
    for i in node[cur]:
        if seen[i] == False:
            dfs(i)

# 最大公約数(互除法)
def GCD(A, B):
	while A >= 1 and B >= 1:
		if A >= B:
			A = A % B
		else:
			B = B % A
	if A >= 1:
		return A
	return B

# 文字列ハッシュ化(使うときはl38以下コピペ)
class StringHash:
    #アルファベットを0-25の整数に変換
    t = list(map(lambda c: (ord(c) - ord('a')), s))

    #100**nを前計算
    mod = 10**9 + 7
    power100 = [1] * (n + 1)
    for i in range(n):
        power100[i + 1] = power100[i] * 100 % mod

    #h[i] := 先頭からi文字目までのハッシュ値
    h = [0] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * 100 + t[i]) % mod

    #ハッシュ値を計算する関数
    def get_hash(l, r):
        return (h[r] - h[l - 1] * power100[r - l + 1]) % mod
