N = int(input())
L = set(tuple(map(int,input().split())) for _ in range(N))
print(len(L))