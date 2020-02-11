# amount of days of a given month
m = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def count_days(startyear, endyear):
    days = 0
    for y in range(startyear, endyear):
        days += 365
        if is_leap_year(y):
            days += 1
    return days


# always start on a monday
def sunday_indices(startyear, endyear):
    return list(range(7, count_days(startyear, endyear), 7))


def fom_indices(startyear, endyear):
    return
