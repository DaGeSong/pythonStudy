# Abstract Data Types
# This program defined a new ADT - Bag, details as below:

class Bag(object):
    # define constructor method, this maxsize for the bag is 60
    def __init__(self, maxsize=60):
        self.maxsize = maxsize
        self._items = list()

    def add(self, item):
        if len(self) >= self.maxsize:
            raise Exception('Full')
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()
    print(bag.maxsize)

    bag.add(1)
    bag.add(2)
    bag.add(3)

    print(bag._items)
    assert len(bag) == 3
    bag.remove(3)
    assert len(bag) == 2
    for i in bag:
        print(i)


if __name__ == '__main__':
    test_bag()
