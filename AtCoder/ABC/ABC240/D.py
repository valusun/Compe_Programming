def main():
    _ = int(input())
    A = list(map(int, input().split()))
    cylinder = [[-1, 0]]
    ans = 0
    for a in A:
        if cylinder[-1][0] == a:
            cylinder[-1][1] += 1
            ans += 1
            if cylinder[-1][1] == a:
                cylinder.pop()
                ans -= a
        else:
            cylinder.append([a, 1])
            ans += 1
        print(ans)


if __name__ == "__main__":
    main()
