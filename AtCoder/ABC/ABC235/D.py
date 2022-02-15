from collections import deque

a,N = map(int,input().split())

Q = deque()
Q.append((1, 0))

Seen = set()
Seen.add(1)

while Q:
    Num, d = Q.popleft()
    if Num == N:
        print(d)
        break

    if len(str(Num*a)) <= len(str(N)):
        Q.append((Num*a, d+1))
        Seen.add(Num*a)

    if Num >= 10 and Num%10!=0:
        new_Num = int(str(Num)[-1] + str(Num)[:-1])
        if new_Num not in Seen:
            Q.append((new_Num, d+1))
            Seen.add(new_Num)

else:
    print(-1)