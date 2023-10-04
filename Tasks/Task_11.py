a = int(input("Enter number a: "))
b = int(input("Enter number b (b should be greater than or equal to a and not greater than 200): "))

if b > 200:
    print("The number b should not be greater than 200. Please enter valid values.")
else:
    total_sum = 0

    count = 0

    for number in range(a, b + 1):
        total_sum += number
        count += 1

    average = total_sum / count

    print(f"The arithmetic mean of all integers from {a} to {b} inclusive is: {average}")