def main():
    N = int(input())
    restaurants = [list(input().split()) + [i + 1] for i in range(N)]
    restaurants = sorted(restaurants, key=lambda x: (x[0], -int(x[1])))
    print(*[restaurants[i][2] for i in range(N)], sep="\n")


if __name__ == "__main__":
    main()
