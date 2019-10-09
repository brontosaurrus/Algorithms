def binary_search(list, item):
    low, high = 0, len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if item > list[mid]:
            low = mid + 1
        elif item < list[mid]:
            high = mid - 1
        else:
            return mid
    raise ValueError("{} not in list".format(item))
    
print(binary_search([2,5,7,8,9,11,14,16], 14))