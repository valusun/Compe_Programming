def Check(h, m):
    h, m = str(h).zfill(2), str(m).zfill(2)
    hour, minute = f"{h[0]}{m[0]}", f"{h[1]}{m[1]}"
    return 0 <= int(hour) < 24 and 0 <= int(minute) < 60


def main():
    H, M = map(int, input().split())
    while not Check(H, M):
        M += 1
        if M == 60:
            H += 1
            M = 0
        if H == 24:
            H = 0
    print(H, M)


if __name__ == "__main__":
    main()
