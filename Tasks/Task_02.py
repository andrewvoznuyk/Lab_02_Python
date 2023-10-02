year = int(input("Введіть номер року: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_year = 366
else:
    days_in_year = 365

print(f"Amount of days in year {year}: {days_in_year} days")

