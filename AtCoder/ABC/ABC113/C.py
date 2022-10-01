def main():
    _, M = map(int, input().split())
    cities = []
    for i in range(M):
        cities.append(list(map(int, input().split())) + [i])
    cities.sort()

    ans = []
    now_p, x = cities[0][0], 1
    for p, _, i in cities:
        if now_p != p:
            x = 1
            now_p = p
        ans.append([f"{str(p).zfill(6)}{str(x).zfill(6)}", i])
        x += 1
    ans.sort(key=lambda x: x[1])

    for a, _ in ans:
        print(a)


if __name__ == "__main__":
    main()
