# 10進数valueをbase進数変換(2 <= base <= 9)
def base10int(value,base):
    A = []
    while value > 0:
        A.append(str(value % base))
        value //= base
    return  int(''.join(A[::-1]))

# 深さ優先探索(dfs) curをrootとし、通ったnodeをTrueとする。
# True数がnodeの個数と一致するとき、nodeは連結である。
def dfs(cur):
    seen[cur] =True
    for i in node[cur]:
        if seen[i] == False:
            dfs(i)

# bit全探索
def Enumerate(list):
    for i in range(1 << len(list)): #全パターン調べる。i.e. range(2 ** len(list))
        for j in range(len(list)): #各ビット調べる
            if i >> j & 1: #j番目のbitが立ってるか
                #bitが立っているときにする処理
    return

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

# セグ木(l58以下)
class SegmentTree:
    ##### segfunc#####
    def segfunc(x, y):
        return max(x, y)
    #################

    ##### ide_ele#####
    ide_ele = -10**18
    #################

    class SegTree:
        """
        init(init_val, ide_ele): 配列init_valで初期化 O(N)
        update(k, x): k番目の値をxに更新 O(logN)
        query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
        """
        def __init__(self, init_val, segfunc, ide_ele):
            """
            init_val: 配列の初期値
            segfunc: 区間にしたい操作
            ide_ele: 単位元
            n: 要素数
            num: n以上の最小の2のべき乗
            tree: セグメント木(1-index)
            """
            n = len(init_val)
            self.segfunc = segfunc
            self.ide_ele = ide_ele
            self.num = 1 << (n - 1).bit_length()
            self.tree = [ide_ele] * 2 * self.num
            # 配列の値を葉にセット
            for i in range(n):
                self.tree[self.num + i] = init_val[i]
            # 構築していく
            for i in range(self.num - 1, 0, -1):
                self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])
        
        def update(self, k, x):
            """
            k番目の値をxに更新
            k: index(0-index)
            x: update value
            """
            k += self.num
            self.tree[k] = x
            while k > 1:
                self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
                k >>= 1

        def query(self, l, r):
            """
            [l, r)のsegfuncしたものを得る
            l: index(0-index)
            r: index(0-index)
            """
            res = self.ide_ele

            l += self.num
            r += self.num
            while l < r:
                if l & 1:
                    res = self.segfunc(res, self.tree[l])
                    l += 1
                if r & 1:
                    res = self.segfunc(res, self.tree[r - 1])
                l >>= 1
                r >>= 1
            return res

# Union-Find木
class UnionFind:
    # n頂点のUnion-Find木を生やす
    # 親を表す配列とグループのサイズを表す配列を用意する
    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n
    
    # 頂点xの根を求める関数を定義する
    def root(self, x):
        # 根にたどり着くまで親をたどる
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    # 頂点u,vを統合する関数を定義する
    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        
        # 既に統合されているなら何もしない
        if root_u == root_v:
            return

        # 頂点数の多い方に統合する（これにより計算量が抑えられる）
        if self.siz[root_u] < self.siz[root_v]:
            self.par[root_u] = root_v
            self.siz[root_v] += self.siz[root_u]
        else:
            self.par[root_v] = root_u
            self.siz[root_u] += self.siz[root_v]

    # 頂点u,vが同じグループに属するか判定する関数を定義する
    def same(self, u, v):
        return self.root(u) == self.root(v)