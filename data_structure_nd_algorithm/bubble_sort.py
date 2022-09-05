# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

def bubble_sort(elements):
    swapped = False
    temp = None

    # needs len(elements) -1 times out layer iterations
    for j in range(len(elements)-1):
        # for the inside loop, needs len(elements)-1-j times iterations
        for i in range(len(elements) - 1 - j):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = temp
                swapped = True
        # if the swapped remains False after one full cycle iteration, that means the list is a sorted list already, no need to continue
        if not swapped:
            break


if __name__ == '__main__':
    # elements = [5, 9, 2, 1, 67, 34, 88, 34, 5, 98, 65, 82]
    elements = [9, 9, 6]
    # elements = [1, 2, 3]
    # elements = []
    bubble_sort(elements)
    print(elements)
