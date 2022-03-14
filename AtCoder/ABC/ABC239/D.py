from math import sqrt

A,B,C,D = map(int,input().split())

def prime_check(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

for i in range(A,B+1):
    for j in range(C,D+1):
        if prime_check(i+j):
            break
    else:
        print("Takahashi")
        exit()
print("Aoki")