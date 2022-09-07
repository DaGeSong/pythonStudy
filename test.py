def find_min(elements):
    if len(elements) > 0:
        min_index = 0
        for i in range(1, len(elements)):
            min = elements[min_index]
            if elements[i] < min:
                min_index = i
        return min_index
    return None


def selection_sort(elements):
    newlist = []
    # print(type(newlist))

    while len(elements) > 0:
        min_index = find_min(elements)
        newlist.append(elements.pop(min_index))
    return newlist


elements = [11, 9, 29, 7, 2, 15, 28, 56, 5, 4, 90, 88, 9, 2, 7]
print(selection_sort(elements))
