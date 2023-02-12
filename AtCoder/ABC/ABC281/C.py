def main():
    N, T = map(int, input().split())
    song_times = list(map(int, input().split()))
    amount = T % sum(song_times)
    for i, t in enumerate(song_times, 1):
        if t < amount:
            amount -= t
        else:
            print(i, amount)
            break


if __name__ == "__main__":
    main()
