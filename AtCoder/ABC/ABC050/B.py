def main():
    _ = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    problems_times = [list(map(int, input().split())) for _ in range(M)]
    all_solving_time = sum(T)
    for p, t in problems_times:
        print(all_solving_time - T[p - 1] + t)


if __name__ == "__main__":
    main()
