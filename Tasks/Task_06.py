def calculate_triangle_area(base, height):
    return 0.5 * base * height

base = float(input("Enter the base length of the triangle (a): "))
height = float(input("Enter the height of the triangle (h): "))

area = calculate_triangle_area(base, height)

if area % 2 == 0:
    area /= 2
    print("Area of the triangle:", area)
else:
    print("Cannot divide by 2!")