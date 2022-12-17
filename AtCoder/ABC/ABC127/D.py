import heapq


def main():
    _, M = map(int, input().split())
    sequence = list(map(int, input().split()))
    query = list(list(map(int, input().split())) for _ in range(M))
    query.sort(key=lambda x: x[1], reverse=True)

    heapq.heapify(sequence)
    for w_cnt, w_num in query:
        is_writing = False
        for i in range(w_cnt):
            x = heapq.heappop(sequence)
            if x < w_num:
                heapq.heappush(sequence, w_num)
                is_writing = True
            else:
                heapq.heappush(sequence, x)
        if not is_writing:
            break
    print(sum(sequence))


if __name__ == "__main__":
    main()
