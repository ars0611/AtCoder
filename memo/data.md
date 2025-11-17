# データ構造関連   
## deque   
- `popleft()`, `pop()`で高速にpopができる   
- 添え字を扱える   
## heapq   
- `heapq.heapify(list)`でlistを優先度付きキューに変換   
- `heapq.heappush(list, value)`でlistにvalueをpush   
- `heapq.heappop(list)`listからminをpop   
- すなわち、heapqでmaxをpopしたければ、符号を反転して格納すればよい   
## set   
- 重複を許さない集合   
```python: example.py
num = 1
s = set([0, 2, 5, 8, 3])
print(num in set) # False. numがsetにあるかO(1)で参照
```   
## sortedcontaiers   
- from sortedcontainers import SortedSet, SortedList, SortedDict
- 勝手にsortしてくれる上ににぶたんも備わっている最強データ構造
- ローカルで使う際は`pip install sortedcontainers`   
- tatyam-SortedSetの方が速いらしい。[リンク](https://github.com/tatyam-prime/SortedSet)
## dict   
- `defaultdict(int)` はすべてのkeyのvalueを指定の型で初期化する   
```python: example.py
d = dict()
for value in d.values(): #valueについてすべて参照できる。.keys()とするとkeyについても同様。itemだとkey, valueが返る
    print(value)
```   
## stack   
- 後入れ先出しなデータ構造   
- listでやるだけ   
- 部分文字列の削除などで使いがち
## list   
- listは=でつなぐとイテレータを渡しているのか、連動してしまう
```python: example.py
# 誤ったコピー
a = [0, 1, 2, 3]
b = a
print(b)        # [0, 1, 2, 3]
a[0] = 4
print(b)        # [4, 1, 2, 3]
```
```python: example.py
# 正しいコピー
a = [0, 1, 2, 3]
b = a[:]
print(b)        # [0, 1, 2, 3]
a[0] = 4
print(b)        # [0, 1, 2, 3]
```   
## str
- strは**イミュータブル**なので、str内の一文字を変更などし得る場合は、listで一文字ずつもつのがベスト   
## RollingHash   
- 文字列をb進数の数字に変換（ハッシュ値）して管理するアルゴリズム    
- b*(ord(ch) - ord(a))で1文字ずつb進数に変換して素数modとって文字列をハッシュ化
- 有名modを撃墜されたら**base**を変えると良い
## SegmentTree   
- 各セルに区間に関する情報を持つ。深くなるたびに扱う区間の長さが半分にされる
- O(logn)で指定の区間に指定の操作をできる   
- セグ木は値の更新がある累積和や累積maxminで有効   
