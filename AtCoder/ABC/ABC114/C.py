import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    def dfs(n: int, bit: int):
        if n > N:
            return 0
        res = 1 if bit == 0b111 else 0
        res += dfs(n * 10 + 3, bit | 0b001)
        res += dfs(n * 10 + 5, bit | 0b010)
        res += dfs(n * 10 + 7, bit | 0b100)
        return res

    print(dfs(0, 0))


if __name__ == "__main__":
    main()
