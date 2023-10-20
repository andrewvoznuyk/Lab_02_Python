n = int(input("Enter a value for 'n': "))

current_number = 1
difference = 1

def generate_sequence(n):
    sequence = [1]
    odd_number = 1

    while len(sequence) < n:
        next_term = sequence[-1] + odd_number
        if next_term >= n:
            print(next_term)
            break
        sequence.append(next_term)
        odd_number += 2

    return sequence

sequence = generate_sequence(n)

print(f"The first number greater than {n} in the sequence is: {current_number}")