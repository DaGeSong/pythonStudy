# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
# and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.


# Normal binary search algorithm for sorted list, Assuming no repetitive items on the list
# 1: Compare middle item to the query
# 2: if they are eqaul, return the relevant index
# 3: if query > middle item, then go to do the search on first half
# 4: if query < middle item, then go to the search on the second half
# 5: repeat the process 1-4 until find the equivalent item, or None for searching out the whole list without finding it

def locate_card(query, cards):
    low = 0
    high = len(cards) - 1

    while high >= low:
        mid = (low + high) // 2
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            high = mid - 1
        else:
            low = mid + 1
    return None


# cards = [80, 77, 65, 58, 55, 54, 45, 34, 32, 12, 8, 6, 4, 2, 1]
# query = 65

# cards = [90]
# query = 9

# cards = [80, 77, 65, 58, 55, 54, 45, 34, 32, 12, 8, 6, 4, 2, 1]
# query = 80

# cards = [80, 77, 65, 58, 55, 54, 45, 34, 32, 12, 8, 6, 4, 2, 1]
# query = 1

cards = [80, 77, 65, 58, 55, 54, 45, 34, 32, 12, 8, 6, 4, 2, 1]
query = 77

result = locate_card(query, cards)
print('this is for non-repetitve cards list & Iterative method:', result)


# binary search recursive method
def locate_card_recursive(low_position, high_position, cards_list, query_number):
    while high_position >= low_position:
        mid = (low_position + high_position) // 2
        if cards_list[mid] == query_number:
            return mid
        elif cards_list[mid] > query_number:
            return locate_card_recursive(mid+1, high_position, cards_list, query_number)
        else:
            return locate_card_recursive(low_position, mid - 1, cards_list, query_number)
    return None


cards_list = [80, 77, 65, 58, 55, 54, 45, 34, 32, 12, 8, 6, 4, 2, 1]
query_number = 45

result_recursive = locate_card_recursive(
    0, len(cards_list) - 1, cards_list, query_number)
print('this is for non-repetitve cards list & recursive method:', result_recursive)


# for repetitive items in the card list, we have to have extra step to find the first occurrence

cards = [80, 77, 65, 58, 55, 55, 54, 45, 34, 32, 12, 8, 6, 4, 2, 1]
query = 55
result = locate_card(query, cards)
# this will print wrong answer, because 55 appeared on the position 4 and 5, however the result will give position 5
print('non-repetitve cards list & Iterative method will give wrong answer for the repetitive list: ', result)


def locate_card_repetitive(cards_repetitive, query_repetitive):
    low = 0
    high = len(cards_repetitive) - 1
    while high >= low:
        mid = (low + high) // 2
        if cards_repetitive[mid] == query_repetitive:
            if cards_repetitive[mid - 1] != query_repetitive:
                return mid
            else:
                high = mid - 1
        elif cards_repetitive[mid] > query_repetitive:
            low = mid + 1
        else:
            high = mid - 1
    return None


cards_repetitive = [80, 77, 65, 58, 55, 55, 54, 45, 34, 32, 12, 8, 6, 4, 2, 1]
query_repetitive = 40
better_result = locate_card_repetitive(cards_repetitive, query_repetitive)
print('this repetitive method will give accurate answer for the repetitive list: ', better_result)
