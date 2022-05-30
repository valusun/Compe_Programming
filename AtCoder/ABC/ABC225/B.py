def main():
    N = int(input())
    edge_cnts = [0] * N
    for i in range(N - 1):
        v, u = map(int, input().split())
        edge_cnts[v - 1] += 1
        edge_cnts[u - 1] += 1
    if max(edge_cnts) == N - 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
