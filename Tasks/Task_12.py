a = int(input("Enter number a: "))
b = int(input("Enter number b (b should be greater than or equal to a): "))

total_sum = 0
current_number = a

while current_number <= b:
    total_sum += current_number
    current_number += 1

print(f"The sum of all integers from {a} to {b} inclusive is: {total_sum}")