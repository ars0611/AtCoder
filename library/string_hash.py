class StringHash:
    def __init__(self, s, base, mod):
        self.n = len(s)
        self.mod = mod
        self.base = base

        # アルファベットを 0〜25 に変換
        t = [ord(ch) - ord('a') for ch in s]

        # base**i を前計算
        self.power = [1] * (self.n + 1)
        for i in range(self.n):
            self.power[i + 1] = self.power[i] * self.base % self.mod

        # h[i] := 先頭から i 文字目までのハッシュ値
        self.h = [0] * (self.n + 1)
        for i in range(self.n):
            self.h[i + 1] = (self.h[i] * self.base + t[i]) % self.mod

    # sのl - 1文字目からr文字目までのハッシュ値
    def get_hash(self, l, r):
        return (self.h[r] - self.h[l] * self.power[r - l]) % self.mod
