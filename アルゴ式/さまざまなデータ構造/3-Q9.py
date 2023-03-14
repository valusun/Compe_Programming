def main():
    N, Q = map(int, input().split())
    follow_state = [[] for _ in range(N)]

    for _ in range(Q):
        n, *q = map(int, input().split())
        if n == 0:
            following_user, followed_user = q
            if following_user in follow_state[followed_user]:
                continue
            follow_state[followed_user].append(following_user)
        else:
            user = q[0]
            if not follow_state[user]:
                print("No")
                continue
            follow_state[user] = sorted(follow_state[user])
            print(*follow_state[user])


if __name__ == "__main__":
    main()
