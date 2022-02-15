N = int(input())
N_len = len(str(N))

MOD = 998244353

# bit : i桁目であり得るf(x)の最大数(0,9,90,900,...)
# 1桁目では、f(9)=9が最大、2桁目では、f(99)=90が最大,...
bit = [0]

# bit_9 : i桁の最大数(0,9,99,999,...)
bit_9 = [0]
for i in range(20):
    bit.append(9*(10**i))
    bit_9.append(int('9'*(i+1)))

Ans = 0
for i in range(N_len-1):
    # 1 ~ f(x)の総和
    Ans += (bit[i+1]*(bit[i+1]+1))//2
    Ans %= MOD

X = N-bit_9[N_len-1]
print((Ans+(X*(X+1)//2))%MOD)