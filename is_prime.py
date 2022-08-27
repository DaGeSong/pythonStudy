# judge a given numer is a prime number or no
# prime number is "A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself."
def is_prime(num):
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
# test to see if num can be divided by any number below it, if not, return True to prime number


for i in range(1, 100):
    if is_prime(i+1):
        print(i+1, end=" ")
print("\n ................this is stupid method, testing all the numbers below give number...................")


#............................................................................................#
# version 2 to utilize the best algorithm
# check till √n because a larger factor of n must be a multiple of a smaller factor that has been already checked

def is_prime_ver2(num):
    if num > 1:
        for i in range(2, int(num**.5) + 1):
            if num % i == 0:
                return False
        else:
            return True


for i in range(1, 100):
    if is_prime_ver2(i+1):
        print(i+1, end=" ")
print("\n...................this is better algorithm...................")
