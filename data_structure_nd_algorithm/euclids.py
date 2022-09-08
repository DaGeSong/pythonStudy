# Euclid’s algorithm, will use divide and conquer methodology to implement it
# this function will return the side of the biggest square with any give rectangles(long and short)
def dnc(long, short):
    if long % short == 0:
        return short
    while long % short != 0:
        temp = short
        short = long % short
        long = temp
        return dnc(long, short)


long = 640
short = 400

print(f'the biggest square\'s side can get from this is {dnc(long, short)}')


# Second function will use D&C to get the sum of all items in a given array
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(sum([1, 2, 3, 4, 5, 6]))


# Third function will use D&C to get the counts of all items in a given array
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(count([1, 2, 3, 4, 5, 6, 7, 8, 9]))
