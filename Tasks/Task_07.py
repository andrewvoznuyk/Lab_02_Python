months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_number = int(input("Enter a number from 1 to 12: "))

if 1 <= month_number <= 12:
    month_name = months[month_number - 1]
    print("Month:", month_name)
else:
    print("Invalid number. Please enter a number from 1 to 12.")