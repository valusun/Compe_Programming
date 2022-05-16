import heapq


def main():
    Q = int(input())
    bag = []
    heapq.heapify(bag)
    offset = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(bag, query[1] - offset)
        elif query[0] == 2:
            offset += query[1]
        else:
            print(heapq.heappop(bag) + offset)


if __name__ == "__main__":
    main()
