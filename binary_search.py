# File to practice binary search method

import linear_search, recursive_binary_search # type: ignore

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

def binary_search(list, target):
    # Function that finds an index in a list by O(log n) time complexity
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    # function to verify the code for binary search
    if index is not None:
        return print("Number found at index: ", index)
    else:
        return print("Not found in list")

if __name__ == '__main__':
    # test cases
    verify(linear_search.linear_search(list, 12))
    recursive_binary_search.verify(recursive_binary_search.recursive_binary_search(list, 12))
    for i in range(0, 25, 4):
        verify(binary_search(list, i))