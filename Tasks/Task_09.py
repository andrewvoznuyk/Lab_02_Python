while True:
    A = int(input("Enter number A: "))
    B = int(input("Enter number B (B should be greater than A): "))
    if A < B:
        break


# Initialize a variable to store the sum
total_sum = 0

# Loop to calculate the sum of numbers from A to B
for number in range(A, B + 1):
    total_sum += number

# Display the result
print(f"The sum of all integers from {A} to {B} inclusive is: {total_sum}")