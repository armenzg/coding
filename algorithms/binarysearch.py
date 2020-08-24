# Watch: https://www.youtube.com/watch?v=P3YID7liBug
# I need to retry this. The trick is looking closing at the middle index
def binarySearch(list, value):
    if len(list) == 0:
        return -1
    return _binarySearchIterative(list, value)
    # return _binarySearch(list, 0, len(list)-1, value)

def _binarySearch(list, low, high, value):
    # initialize low = 0, high = N, mid = (low + high)/2
    # check if element is at position mid; if found, return
    # else depending upon value of mid is lower or greater,
    # we explore the high side of the array or the low side
    if (low > high):
        return -1

    middle = int((low + high) / 2)
    if list[middle] > value:
        return _binarySearch(list, low, middle - 1, value)
    elif list[middle] < value:
        return _binarySearch(list, middle + 1, high, value)
    else:
        return middle

# Less memory consumption
def _binarySearchIterative(list, value):
    low = 0
    high = len(list)

    while (low <= high):
        middle = int((low + high) / 2)
        if list[middle] > value:
            high = middle - 1
        elif list[middle] < value:
            low = middle + 1
        else:
            return middle

    return -1

if __name__ == "__main__":
    assert binarySearch([], 12) == -1
    assert binarySearch([1,2,3,10,12,13], 12) == 4
    assert binarySearch([1,2,3,10,12,13], 13) == 5
    assert binarySearch([1,2,3,10,12,13], 2) == 1
    assert binarySearch([1,2,3,10,12,13], 1) == 0