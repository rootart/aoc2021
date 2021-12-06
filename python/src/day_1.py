from typing import List


def get_inputs() -> List[int]:
    inputs = []
    with open("./inputs/day_1.txt") as f:
        for line in f.readlines():
            inputs.append(int(line.strip()))
    return inputs


def solution_a(inputs: List[int]) -> int:
    increase_counter = 0
    for index, value in enumerate(inputs):
        if index < len(inputs) - 1 and value < inputs[index + 1]:
            increase_counter += 1
    return increase_counter


def solution_b(inputs: List[int]) -> int:
    window_size = 3
    index = 0
    moving_sum = []
    while index < len(inputs) - window_size + 1:
        window = inputs[index: index + window_size]
        moving_sum.append(sum(window))
        index += 1
    return solution_a(moving_sum)


def run():
    inputs = get_inputs()
    print(f"Solution for part (a): {solution_a(inputs)}")
    print(f"Solution for part (b): {solution_b(inputs)}")


if __name__ == '__main__':
    run()
