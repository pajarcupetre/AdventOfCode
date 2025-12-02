def decode_password(rotations):
    counts_of_zero = 0
    position = 50
    for rotation in rotations:
        direction = rotation[0]
        steps = int(rotation[1:])
        if direction == 'L':
            position -= steps
        elif direction == 'R':
            position += steps
        position %= 100
        if position == 0:
            counts_of_zero += 1 
    return counts_of_zero

def decode_password_with_click(rotations):
    counts_of_zero = 0
    position = 50
    for rotation in rotations:
        direction = rotation[0]
        steps = int(rotation[1:])
        if direction == 'L':
            original_position = position
            position -= steps
            if position < 0 and original_position > 0:
                counts_of_zero += (-position - 1) // 100 + 1
            if position % 100 == 0:
                counts_of_zero += 1
        elif direction == 'R':
            position += steps
            counts_of_zero += position // 100
        position %= 100
    return counts_of_zero

if __name__ == "__main__":
    with open("2025/inputs/day1_input_short.txt", "r") as file:
        rotations = file.read().strip().split("\n")
    result = decode_password(rotations)
    print(f"Number of times position 0 is reached with v1: {result}")
    result = decode_password_with_click(rotations)
    print(f"Number of times position 0 is reached with v2: {result}")
