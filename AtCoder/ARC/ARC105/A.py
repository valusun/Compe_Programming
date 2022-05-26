def main():
    cookies = sorted(list(map(int, input().split())))
    if cookies[0] + cookies[3] == sum(cookies[1:3]) or sum(cookies[:3]) == cookies[3]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
