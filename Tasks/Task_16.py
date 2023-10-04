n = int(input("Enter a value for 'n': "))

current_number = 1
difference = 1

while current_number <= n:
    current_number += difference
    difference += 1

print(f"The first number greater than {n} in the sequence is: {current_number}")