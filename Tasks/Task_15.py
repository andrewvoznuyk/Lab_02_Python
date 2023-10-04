n = int(input("Enter a value for 'n': "))

result = None

for number in range(1, n + 1):
    square = number ** 2

    if square > n:
        result = square
        break

if result is not None:
    print(f"The first number greater than {n} in the sequence is: {result}")
else:
    print(f"No number greater than {n} was found in the sequence.")
