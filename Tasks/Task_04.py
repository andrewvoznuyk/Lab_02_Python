import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

min_num = min(num1, num2, num3, num4)

cos_min_num = math.cos(min_num)

print(f"Minimum number: {min_num}")
print(f"Cosine of the minimum number: {cos_min_num}")