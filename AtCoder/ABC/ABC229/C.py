def main():
    N, W = map(int, input().split())
    Cheese = []
    for _ in range(N):
        Cheese.append(list(map(int, input().split())))
    Cheese.sort(reverse=True)
    now_taste, now_weight = 0, 0
    for t, w in Cheese:
        if now_weight + w <= W:
            now_taste += t * w
            now_weight += w
        else:
            now_taste += t * (W - now_weight)
            break
    print(now_taste)


if __name__ == "__main__":
    main()
