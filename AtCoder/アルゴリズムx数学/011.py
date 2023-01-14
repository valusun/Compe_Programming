def GetPrimes(n: int):
    primes = [False, True] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = False
    primes[2] = True
    for p in range(3, int(n**0.5) + 1, 2):
        if not primes[p]:
            continue
        for q in range(p * p, n + 1, 2 * p):
            primes[q] = False
    return primes


def main():
    ans = [i for i, p in enumerate(GetPrimes(int(input()))) if p]
    print(*ans)


if __name__ == "__main__":
    main()
