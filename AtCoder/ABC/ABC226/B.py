def main():
    N = int(input())
    ans = set()
    for _ in range(N):
        _, *a = map(int, input().split())
        ans.add(tuple(a))
    print(len(ans))


if __name__ == "__main__":
    main()
