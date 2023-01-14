def main():
    def dfs(n):
        if n == 1:
            return 1
        return dfs(n - 1) * n

    print(dfs(int(input())))


if __name__ == "__main__":
    main()
