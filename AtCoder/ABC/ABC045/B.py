def main():
    cards = [list(input()) for _ in range(3)]
    toindex = dict(a=0, b=1, c=2)
    turn = 0
    while True:
        if not cards[turn]:
            break
        turn = toindex[cards[turn].pop(0)]
    print(chr(turn + 65))


if __name__ == "__main__":
    main()
