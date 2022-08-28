# fibonacci list
# the first element of the sequence is equal to one (Fib1 = 1)
# the second is also equal to one (Fib2 = 1)
# every subsequent number is the the_sum of the two preceding numbers: (Fibi = Fibi-1 + Fibi-2)


# use recursive function to get the fibonacci number at position "position"
def fibonacci_num_rec(position):
    if position == 1:
        return 1
    elif position == 2:
        return 1
    else:
        return fibonacci_num_rec(position-1) + fibonacci_num_rec(position-2)


# use normal non-recursive way to implement it
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


# use created fibonacci_rec function to get the whole fibonacci list with given num (how many numbers in the list)
def fibonacci_list_rec(num):
    fibonacci_list_rec = []
    for i in range(num):
        fibonacci_list_rec.append(fibonacci_num_rec(i+1))
    return fibonacci_list_rec


print(fibonacci_list_rec(9))

for n in range(1, 10):  # testing
    print(n, "->", fib(n))
