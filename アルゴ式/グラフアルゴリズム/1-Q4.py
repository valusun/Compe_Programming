def main():
    N, M, X = map(int, input().split())
    friends = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    aruru_friends = set(friends[X])
    friend_friends = set([f for i in friends[X] for f in friends[i]])
    print(len(friend_friends - aruru_friends - set([X])))


if __name__ == "__main__":
    main()
