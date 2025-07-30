# File to practice the recursive method for binary search

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

def recursive_binary_search(list, target):
    # Function that finds an item in a list with O(log n) time complexity
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(index):
    # function to verify the code for the recursive binary search
    if index is not None:
        return print("Target found at index: ", index)
    else:
        return print("Not found in list")

# test cases
verify(recursive_binary_search(list, 0))
verify(recursive_binary_search(list, 1))
verify(recursive_binary_search(list, 5))
verify(recursive_binary_search(list, 10))
verify(recursive_binary_search(list, 13))
verify(recursive_binary_search(list, 17))
verify(recursive_binary_search(list, 24))
verify(recursive_binary_search(list, 25))
verify(recursive_binary_search(list, 30))
verify(recursive_binary_search(list, 100))