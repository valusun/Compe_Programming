N = int(input())

if N==1:
    print(1)
    exit()

Ans = 0
for A in range(1, N):
    if A**3 > N:
        break
    for B in range(A, N):
        C = N//(A*B)
        if C>=B:
            Ans+=(C-B+1)
        else:
            break

print(Ans)
