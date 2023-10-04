N = int(input("Enter an integer N (> 1): "))

if N <= 1:
    print("Please enter an integer greater than 1.")
else:
    K = 0
    result = 1

    while result <= N:
        K += 1
        result = 5 ** K

    print(f"The smallest integer K for which 5^K > {N} is: {K}")