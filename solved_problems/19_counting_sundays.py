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


def days_in_month(month, year):
    if month == 2 and is_leap_year(year):
        return 29

    return m[month]

def increment_day(weekday, day, month, year):
    day += 1

    if day > days_in_month(month, year):
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1
    
    weekday = (weekday + 1) % 7

    return weekday, day, month, year


def count_sundays_on_first_of_month(start_day, start_month, start_year, end_day, end_month, end_year):

    date = 2, start_day, start_month, start_year
    sundays = 0

    weekday, day, month, year = date

    while (day, month, year) != (end_day, end_month, end_year):
        if weekday == 6 and day == 1:
            sundays += 1
        
        date = increment_day(*date)
        weekday, day, month, year = date

    return sundays


sundays = count_sundays_on_first_of_month(1, 1, 1901, 31, 12, 2000)
print(sundays)