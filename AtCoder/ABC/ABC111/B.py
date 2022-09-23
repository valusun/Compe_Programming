from bisect import bisect_left


def main():
    N = int(input())
    contest = [i * 111 for i in range(1, 10)]
    print(contest[bisect_left(contest, N)])


if __name__ == "__main__":
    main()
