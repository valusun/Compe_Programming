def main():
    N = int(input())
    l, r = 1, N
    while r - l > 1:
        mid = (l + r) // 2
        print(f"? {mid}", flush=True)
        n = int(input())
        if n == 0:
            l = mid
        else:
            r = mid
    print(f"! {l}")


if __name__ == "__main__":
    main()
