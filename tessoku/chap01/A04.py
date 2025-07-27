N = int(input())
N_2 =[0]*10 

for i in range(10):
    if N > 0:
        N_2[-i-1] = N % 2
        N //= 2
for i in N_2:
    print(i,end = "")