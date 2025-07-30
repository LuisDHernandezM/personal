# File to practice binary search method

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
        return print("Target found at index: ", index)
    else:
        return print("Not found in list")
    
# test cases
verify(binary_search(list, 0))
verify(binary_search(list, 1))
verify(binary_search(list, 5))
verify(binary_search(list, 10))
verify(binary_search(list, 13))
verify(binary_search(list, 17))
verify(binary_search(list, 24))
verify(binary_search(list, 25))
verify(binary_search(list, 30))
verify(binary_search(list, 100))