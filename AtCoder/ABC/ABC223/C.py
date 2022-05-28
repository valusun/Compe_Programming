def main():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    collision_time = 0
    for i in range(N):
        collision_time += A[i] / B[i] / 2
    point, time = 0, 0
    for i in range(N):
        burn_time = A[i] / B[i]
        if time + burn_time <= collision_time:
            point += A[i]
            time += burn_time
        else:
            point += (collision_time - time) * B[i]
            break
    print(point)


if __name__ == "__main__":
    main()
