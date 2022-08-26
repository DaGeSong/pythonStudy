def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    month_31days = [1, 3, 5, 7, 8, 10, 12]
    month_30days = [4, 6, 9, 11]
    if month in month_31days:
        return 31
    if month in month_30days:
        return 30
    if month == 2:
        if is_year_leap(year) == True:
            return 29
        else:
            return 28


def daysOfyear(year, month, day):
    month = month - 1
    total_day = 0
    while month > 0:
        total_day += days_in_month(year, month)
        month -= 1
    return total_day + day


print(daysOfyear(2022, 1, 25))
