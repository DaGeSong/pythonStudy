# quick sort use D & C
# step 1: for one element list or the empty list, these are already 'sorted', just return them ====>>>> base point for the recursive
# step 2: for other lists, pick the pivot number (first element in the list), and have two new created subarraysto store items less then, and greater then the pivot
# step 3: repeat step 1 and step 2 on the subarrays

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        leftsub = [i for i in list[1:] if i <= pivot]
        rightsub = [i for i in list[1:] if i > pivot]
        return quick_sort(leftsub) + [pivot] + quick_sort(rightsub)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28, 56, 5, 4, 90, 88, 9, 2, 7]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    # # elements = []
    # elements = [6]
    elements = [6, 5, 3, 2, 4, 8]
    print(quick_sort(elements))

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        print(f'sorted array: {quick_sort(elements)}')
