import calendar

# to get input
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar for the given month and year
print("\n", calendar.month_name[month], year)
print(calendar.month(year, month))
