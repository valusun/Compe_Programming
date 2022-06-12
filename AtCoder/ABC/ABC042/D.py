class ModCombination:
    def __init__(self, n=10**6, mod=10**9 + 7):
        self.n = n
        self.mod = mod
        self.fact = [1, 1]
        self.fact_inv = [1, 1]
        self.inv = [0, 1]
        for i in range(2, n):
            self.fact.append(self.fact[-1] * i % self.mod)
            self.inv.append(-self.inv[self.mod % i] * (self.mod // i) % self.mod)
            self.fact_inv.append(self.fact_inv[-1] * self.inv[i] % self.mod)

    def nCk(self, n, k):
        return self.fact[n] * self.fact_inv[n - k] * self.fact_inv[k] % self.mod


def main():
    H, W, A, B = map(int, input().split())
    mc = ModCombination()
    ans = 0
    for i in range(H - A):
        ans += mc.nCk(i + B - 1, i) * mc.nCk(H + W - i - B - 2, H - 1 - i)
        ans %= 10**9 + 7
    print(ans)


if __name__ == "__main__":
    main()
