a = int(input("Enter a value for 'a' (0 ≤ a ≤ 50): "))

if 0 <= a <= 50:
    total_sum_of_squares = 0

    for number in range(a, 51):
        total_sum_of_squares += number ** 2

    print(f"The sum of the squares of integers from {a} to 50 is: {total_sum_of_squares}")
else:
    print("Please enter a valid value for 'a' within the range of 0 to 50.")