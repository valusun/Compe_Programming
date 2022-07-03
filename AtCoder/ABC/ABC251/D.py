def main():
    _ = int(input())
    ans = []
    for i in range(1, 100):
        ans = ans + [i] + [100 * i] + [10000 * i]
    print(len(ans))
    print(*sorted(ans))


if __name__ == "__main__":
    main()
