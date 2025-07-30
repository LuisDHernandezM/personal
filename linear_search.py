# File to practice linear search

import binary_search, recursive_binary_search # type: ignore

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

def linear_search(list, target):
    # Function that finds an index in a list by O(n) time complexity
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    # function to verify the code for linear search
    if index is not None:
        return print("Number found at index: ", index)
    else:
        return print("Not found in list")


if __name__ == '__main__':
    # test cases
    verify(binary_search.binary_search(list, 12))
    recursive_binary_search.verify(recursive_binary_search.recursive_binary_search(list, 12))
    for i in range(0, 25, 4):
        verify(linear_search(list, i))