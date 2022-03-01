N = int(input())
A = input()

for i in range(N):
    if A[i]=='1':
        if i%2==0:
            print("Takahashi")
        else:
            print("Aoki")
        break