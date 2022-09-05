# importing "array" for array operations, using the existing module array
# An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.
from array import array


# initializes array with unicode character
arr = array('u', 'asdf')
print(arr[0], arr[1], arr[2], arr[3])  # look up by index = O(1)


def look_up_by_value(value):  # look up by value = O(n)
    for i in range(len(arr)):
        if arr[i] == value:
            return i


# implementing our own array by using list, set the default constant length to 32
# initializes the array with a default list of 32 None items
class Array(object):
    def __init__(self, size=32):  # our Array will not limit the elements' data type
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):  # rewrite default __getitem__ method
        return self._items[index]

    def __setitem__(self, index, value):  # rewrite default __setitem__ method
        self._items[index] = value

    def __len__(self):  # rewrite default __len__ method
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):  # rewrite default __iter__ method
        for item in self._items:
            yield item  # yield will return a generator


# def a function to test our new Array class
def test_array():
    size = 5
    a = Array(size)
    a[0] = 0
    a[1] = ['yellow', 'blue']
    a[2] = 2.5
    a[3] = {'date': 'Sept 5th', 'event': 'wedding'}
    a[4] = 'song'
    assert a[0] == 0
    assert len(a) == 5
    for i in a:
        print(i)


test_array()

# output:
# 0
# ['yellow', 'blue']
# 2.5
# {'date': 'Sept 5th', 'event': 'wedding'}
# song
