from typing import List


def get_inputs():
    inputs = []
    with open("./inputs/day_2.txt") as f:
        for line in f.readlines():
            command, value = line.split()
            inputs.append([command, int(value)])
    return inputs


def solution_a(inputs) -> int:
    horizontal_position = 0
    depth = 0
    for entry in inputs:
        command, value = entry
        if command == 'up':
            depth = depth - value
        elif command == 'down':
            depth = depth + value
        elif command == 'forward':
            horizontal_position = horizontal_position + value
    print(f'Horizontal position: {horizontal_position}, depth: {depth}')
    return horizontal_position * depth


def solution_b(inputs) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0
    for entry in inputs:
        command, value = entry
        if command == 'up':
            # depth = depth - value
            aim = aim - value
        elif command == 'down':
            # depth = depth + value
            aim = aim + value
        elif command == 'forward':
            horizontal_position = horizontal_position + value
            print(f'aim {(aim * value)}')
            depth = depth + (aim * value)
    print(f'Horizontal position: {horizontal_position}, depth: {depth}')
    return horizontal_position * depth


def run():
    inputs = get_inputs()
    # print(f"Solution for part (a): {solution_a(inputs)}")

    print(f"Solution for part (b): {solution_b(test_inputs)}")


if __name__ == '__main__':
    run()
