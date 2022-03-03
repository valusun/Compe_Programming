N = int(input())
if len(set(list(map(int,input().split())))) == N:
    print("Yes")
else:
    print("No")