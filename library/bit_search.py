# bit全探索
# 2 ** len(list)回探索を回して,各ビットで適切な処理を行う
def bit_search(list):
    for bit in range(1 << len(list)):
        for i in range(len(list)):
            if bit & (1 << i):
                print("下からi番目のbitが立っています")
