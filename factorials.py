# use recursive function to get the factorial answer
def factorials(num):
    if num < 0:
        print("please use a valid positive integer")
        return
    elif num == 1:
        return 1
    else:
        return num * factorials(num-1)


# use iterate way to get the factorial answer
def factorials_iterate(num):
    if num < 0:
        print("please use a valid positive integer")
        return
    elif num == 1:
        return 1
    else:
        answer = 1
        for i in range(2, num+1):
            answer *= i
        return answer


print(factorials(4))
print(factorials_iterate(4))
