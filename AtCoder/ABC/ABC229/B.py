A,B = input().split()
len_A = len(A)
len_B = len(B)

for i in range(min(len_A, len_B)):
    if int(A[len_A-i-1])+int(B[len_B-i-1])>9:
        print("Hard")
        break
else:
    print("Easy")