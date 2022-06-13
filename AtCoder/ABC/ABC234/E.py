from bisect import bisect_left


def GenerateArithmeticProgression():
    sequence = []
    for i in range(1, 10):
        for j in range(-9, 10):
            tmp = ""
            ret = i
            for _ in range(18):
                tmp += str(ret)
                sequence.append(int(tmp))
                ret += j
                if ret < 0 or ret > 9:
                    break
    return sequence


def main():
    N = int(input())
    sequence = sorted(GenerateArithmeticProgression())
    print(sequence[bisect_left(sequence, N)])


if __name__ == "__main__":
    main()
