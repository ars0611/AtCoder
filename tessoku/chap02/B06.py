n = int(input())
a = list(map(int, input().split()))
q = int(input())
sum = [0 for _ in range(n+1)]

for i in range(1,n+1):
    sum[i] = sum[i-1] + a[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    days = r - l + 1
    ans = (sum[r] - sum[l-1]) 
    if ans > days/2:
        print("win")
    elif ans == days/2:
        print("draw")
    else:
        print("lose")