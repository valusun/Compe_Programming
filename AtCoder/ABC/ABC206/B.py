N = int(input())

chokinbako = 0
for i in range(1, 10**9):
    chokinbako += i
    if chokinbako >= N:
        print(i)
        exit()