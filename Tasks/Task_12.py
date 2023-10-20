while True:
    a = int(input("Enter number A: "))
    b = int(input("Enter number B (B should be greater than A): "))
    if b <= a:
        break

total_sum = 0
current_number = a

while current_number <= b:
    total_sum += current_number
    current_number += 1

print(f"The sum of all integers from {a} to {b} inclusive is: {total_sum}")