S1 = input()
S2 = input()
S3 = input()
T = input()

Ans = ""
for i in T:
    if i == '1':
        Ans+=S1
    if i == '2':
        Ans+=S2
    if i == '3':
        Ans+=S3

print(Ans)