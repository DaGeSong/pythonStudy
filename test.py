def binary_search(list, num, low, high):
    while low <= high:
        mid = (low+high)//2
        if list[mid] == num:
            if mid >= 1 and list[mid - 1] == num:
                return binary_search(list, num, low, mid-1)
            return mid
        elif list[mid] > num:
            return binary_search(list, num, low, mid-1)
        else:
            return binary_search(list, num, mid+1, high)
    return None


list = [7, 7]
num = 7

position = binary_search(list, num, 0, len(list)-1)
print(position)
