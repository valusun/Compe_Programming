def main():
    N, K = map(int, input().split())
    array = sorted(list(list(map(int, input().split())) for _ in range(N)))
    cnt = 0
    for a, b in array:
        if cnt + b >= K:
            print(a)
            break
        cnt += b


if __name__ == "__main__":
    main()
