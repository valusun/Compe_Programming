def OutputSequenceWithLength(sequence):
    print(len(sequence), *sequence)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 200
    selected_sum_mod200_indexes = [[] for _ in range(200)]
    for i in range(1, 2**N):
        selected_sum = 0
        selected_indexes = []
        for j in range(N):
            if i & (1 << j):
                selected_sum = (selected_sum + A[j]) % MOD
                selected_indexes.append(j + 1)
        if selected_sum_mod200_indexes[selected_sum]:
            print("Yes")
            OutputSequenceWithLength(selected_indexes)
            OutputSequenceWithLength(*selected_sum_mod200_indexes[selected_sum])
            break
        else:
            selected_sum_mod200_indexes[selected_sum].append(selected_indexes)
    else:
        print("No")


if __name__ == "__main__":
    main()
