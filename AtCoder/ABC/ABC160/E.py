def main():
    X, Y, A, B, C = map(int, input().split())
    R = sorted(list(map(int, input().split())), reverse=True)
    G = sorted(list(map(int, input().split())), reverse=True)
    N = sorted(list(map(int, input().split())), reverse=True)
    chosen = sorted(R[:X] + G[:Y] + N, reverse=True)
    print(sum(chosen[: X + Y]))


if __name__ == "__main__":
    main()
