import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_num = max(num1, num2, num3)

cos_max_num = math.cos(max_num)

print(f"Max number: {max_num}")
print(f"Cosine of the max number: {cos_max_num}")