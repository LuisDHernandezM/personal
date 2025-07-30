# File to practice linear search

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
        return print("Target found at index: ", index)
    else:
        return print("Not found in list")


# test cases
verify(linear_search(list, 0))
verify(linear_search(list, 1))
verify(linear_search(list, 5))
verify(linear_search(list, 10))
verify(linear_search(list, 13))
verify(linear_search(list, 17))
verify(linear_search(list, 24))
verify(linear_search(list, 25))
verify(linear_search(list, 30))
verify(linear_search(list, 100))