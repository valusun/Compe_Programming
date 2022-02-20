N = int(input())
M = []
for i in range(N):
    s,t = input().split()
    M.append([int(t), s])

M.sort(reverse=True)
print(M[1][1])