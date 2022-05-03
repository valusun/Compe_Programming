def main():
    N, K = map(int, input().split())
    human_infos = sorted([list(map(int, input().split())) for _ in range(N)])

    now_town = 0
    for i in range(N):
        if K < human_infos[i][0] - now_town:
            break
        else:
            K = K - human_infos[i][0] + now_town + human_infos[i][1]
            now_town = human_infos[i][0]
    print(now_town + K)


if __name__ == "__main__":
    main()
