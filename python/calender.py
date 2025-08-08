#calender module notes

import calendar

datetime.now().year#this returns current year

#find max days within month
def max_days_in_month(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]#(weekday_of_first_day, number_of_days_in_month)
# Example usage:
print(max_days_in_month(2024, 2))  # Output: 29 (leap year is already acounted for)
print(max_days_in_month(2025, 2))  # Output: 28
print(max_days_in_month(2025, 7))  # Output: 31
