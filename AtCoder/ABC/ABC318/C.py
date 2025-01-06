def main():
    N, D, P = map(int, input().split())
    F = sorted(list(map(int, input().split())), reverse=True)
    ans = 0
    current = 0
    for i, f in enumerate(F, start=1):
        current += f
        if i % D != 0:
            continue
        ans += current if current < P else P
        current = 0
    if current > 0:
        ans += current if current < P else P
    print(ans)


if __name__ == "__main__":
    main()
