N = int(input())
A = list(map(int,input().split()))

Mod = [[] for _ in range(200)]

for i in range(1, 2**N):
    selected_idx = []
    selected_num = 0
    for j in range(N):
        if i&(1<<j):
            selected_num = (selected_num + A[j])%200
            selected_idx.append(j+1)
    if len(Mod[selected_num]):
        print("Yes")
        print(len(Mod[selected_num]), *Mod[selected_num])
        print(len(selected_idx), *selected_idx)
        exit()
    else:
        Mod[selected_num] = selected_idx

print("No")