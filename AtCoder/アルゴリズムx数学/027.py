from typing import List


def MergeSort(A: List[int]) -> List[int]:
    if len(A) == 1:
        return A

    mid = len(A) // 2
    lefts = MergeSort(A[:mid])
    rights = MergeSort(A[mid:])
    left, right = 0, 0
    merged = []
    while left < len(lefts) or right < len(rights):
        if left == len(lefts):
            merged.append(rights[right])
            right += 1
        elif right == len(rights):
            merged.append(lefts[left])
            left += 1
        else:
            if lefts[left] > rights[right]:
                merged.append(rights[right])
                right += 1
            else:
                merged.append(lefts[left])
                left += 1
    return merged


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    print(*MergeSort(A))


if __name__ == "__main__":
    main()
