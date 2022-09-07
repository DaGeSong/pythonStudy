# The selection sort algorithm sorts an array by repeatedly finding the minimum element
# (considering ascending order) from unsorted part and putting it at the beginning.

def selection_sort(elements):
    for i in range(len(elements) - 1):
        low = i
        min_index = i
        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j
        elements[low], elements[min_index] = elements[min_index], elements[low]

    return elements


elements = []
elements = [4]
elements = [4, 4]
elements = ["mona", "dhaval", "aamir", "tina", "chang"]
elements = [5, 3, 1]
elements = [11, 9, 29, 7, 2, 15, 28, 56, 5, 4, 90, 88, 9, 2, 7]
elements = selection_sort(elements)
print(elements)


# method 2, use two functions for this task
# the find_min function will return the index number for the minimal number in the list
def find_min(elements):
    if len(elements) > 0:
        min_index = 0
        for i in range(1, len(elements)):
            min = elements[min_index]
            if elements[i] < min:
                min_index = i
        return min_index
    return None

# the selection_sort_2 function will invoke the find_min function to get the min_index everytime, and pop ou the the item from the original list
# until the original list becomes empty


def selection_sort_2(elements):
    newlist = []
    while len(elements) > 0:
        min_index = find_min(elements)
        newlist.append(elements.pop(min_index))
    return newlist


elements2 = [11, 9, 29, 7, 2, 15, 28, 56, 5, 4, 90, 88, 9, 2, 7]
print(selection_sort_2(elements2))
