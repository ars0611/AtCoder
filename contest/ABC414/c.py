import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
#----------------------------------------#
def base10_to_n(num,base):
    a = []
    while num > 0:
        a.append(str(num % base))
        num //= base
    return ''.join(reversed(a))

def is_pal(num):
    c = 0
    length = len(num)
    while c < length // 2 and num[c] == num[length - 1 - c]:
        c += 1
    return c == length // 2

a = int(input())
n = int(input())
str_n = str(n)
ans = 0
half = 10**((len(str_n)+1)//2)
for i in range(1,half):
    l = str(i)
    r1 = l[::-1]
    r2 = r1[1:]
    pal_1 = int(l + r1)
    pal_2 = int(l + r2)
    if pal_1 <= n and is_pal(base10_to_n(pal_1, a)):
        ans += pal_1
    if pal_2 <= n and is_pal(base10_to_n(pal_2, a)):
        ans += pal_2
    if pal_1 > n and pal_2 > n:
        break
print(ans)

#泣く泣くgptにc++変換してもらったらTLE取れた。このコードがごみなのはわかるけど、そんな重い？