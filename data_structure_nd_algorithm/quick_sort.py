# Quicksort is a sorting algorithm based on the divide and conquer approach where
# An array is divided into subarrays by selecting a pivot element (element selected from the array).
# While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side
# and elements greater than pivot are on the right side of the pivot.
# The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
# At this point, elements are already sorted. Finally, elements are combined to form a sorted array.


# This implementation utilizes pivot as the first element in the list

# partition function will insert pivot number(first element in the list)
# into the right position for any given given list, start index, and end index
# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
