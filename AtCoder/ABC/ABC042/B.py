def main():
    N, _ = map(int, input().split())
    S = [input() for _ in range(N)]
    print("".join(sorted(S)))


if __name__ == "__main__":
    main()
