N = int(input())
Field = [list(input()) for _ in range(N)]

# 縦
def T_check(i,j):
    dot = 0
    for k in range(6):
        if Field[i+k][j] == ".":
            dot+=1
            if dot>2:
                return False
    return True

# 横
def Y_check(i,j):
    dot = 0
    for k in range(6):
        if Field[i][j+k] == ".":
            dot+=1
            if dot>2:
                return False
    return True

# 右下斜め
def R_check(i, j):
    dot = 0
    for k in range(6):
        if Field[i+k][j+k] == ".":
            dot+=1
            if dot>2:
                return False
    return True

# 左下斜め
def L_check(i, j):
    dot = 0
    for k in range(6):
        if Field[i+k][j-k] == ".":
            dot+=1
            if dot>2:
                return False
    return True

for i in range(N):
    for j in range(N):
        if i+6<=N:
            if T_check(i,j):
                print("Yes")
                exit()
            if j+6<=N:
                if R_check(i,j):
                    print("Yes")
                    exit()
            if j-5>=0:
                if L_check(i,j):
                    print("Yes")
                    exit()
        if j+6<=N:
            if Y_check(i,j):
                print("Yes")
                exit()
print("No")
