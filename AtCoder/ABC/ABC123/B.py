from itertools import permutations


def GetTimeForFoodArrival(p):
    """受け取った順序で料理を頼んだ時の時間を返す"""
    result = 0
    for food in p[:-1]:
        result += food
        if mod_time := (food % 10):
            result += 10 - mod_time
    return result + p[-1]


def main():
    A = [int(input()) for _ in range(5)]

    ans = 10**18
    for p in permutations(A):
        ans = min(ans, GetTimeForFoodArrival(p))
    print(ans)


if __name__ == "__main__":
    main()
