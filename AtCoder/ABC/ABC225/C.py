N,M = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(N)]

Flag = True
for i in range(N-1):
    for j in range(M):
        # 必ず配列の下との差は'7'である
        if B[i+1][j]-B[i][j]!=7:
            Flag = False
            break
    if Flag == False:
        break

# B[i][j]%7==0は必ず右端に存在(その右隣は存在しない)
for i in range(M-1):
    if B[0][i]+1!=B[0][i+1] or B[0][i]%7==0:
        Flag = False
        break

if Flag:
    print("Yes")
else:
    print("No")