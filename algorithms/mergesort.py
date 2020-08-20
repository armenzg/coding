SORTED_ARRAY = []

def mergeSort(array, leftStart, rightEnd):
    if leftStart >= rightEnd:
        return

    middlePoint = int((leftStart + rightEnd) / 2);
    mergeSort(array, leftStart, middlePoint)
    mergeSort(array, middlePoint + 1, rightEnd) # The +1 in here is crucial
    # import pdb; pdb.set_trace()
    mergeHalves(array, leftStart, rightEnd)

def mergeHalves(array, leftStart, rightEnd):
    global SORTED_ARRAY
    leftEnd = int((leftStart + rightEnd) / 2)
    rightStart = leftEnd + 1
    size = rightEnd - leftStart + 1;

    left = leftStart
    right = rightStart
    index = leftStart

    while (left <= leftEnd) and (right <= rightEnd):
        if array[left] <= array[right]:
            SORTED_ARRAY[index] = array[left]
            left += 1
        else:
            SORTED_ARRAY[index] = array[right]
            right += 1
        index += 1

    while (left <= leftEnd):
        SORTED_ARRAY[index] = array[left]
        left += 1
        index += 1

    while (right <= rightEnd):
        SORTED_ARRAY[index] = array[right]
        right += 1
        index += 1

    index = leftStart
    # Copy back the sorted elements
    while index <= rightEnd:
        array[index] = SORTED_ARRAY[index]
        index += 1

if __name__ == "__main__":
    a = [1, 5, 2, 11, 9, 33, 2];
    SORTED_ARRAY = [None] * len(a)
    mergeSort(a, 0, len(a) - 1)
    print(a)