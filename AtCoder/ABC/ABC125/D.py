def main():
    _ = int(input())
    A = list(map(int, input().split()))
    B = [abs(a) for a in A]
    negative_num_cnt = len([a for a in A if a < 0])
    print(sum(B) - min(B) * 2 if negative_num_cnt % 2 else sum(B))


if __name__ == "__main__":
    main()
