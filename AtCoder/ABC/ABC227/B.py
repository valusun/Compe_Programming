def ExistArea(area):
    for a in range(1, 200):
        for b in range(1, 200):
            if 4 * a * b + 3 * a + 3 * b == area:
                return True
            if 4 * a * b + 3 * a + 3 * b > area:
                break
    return False


def main():
    _ = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for s in S:
        if not ExistArea(s):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
