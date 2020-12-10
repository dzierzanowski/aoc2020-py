#!/usr/bin/env python3
import string

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data

    index = 25  # Starting after preamble
    termination_index = len(data)

    faulty_index = 0
    faulty_number = 0

    while index < termination_index:
        subset = data[index - 25:index]
        number_at_index = int(data[index])
        is_valid = False
        for number in subset:
            other = number_at_index - int(number)
            if number != other and str(other) in subset:
                # print(f"Found pair for {number_at_index}: {number} and {other}")
                is_valid = True
                break
        if not is_valid:
            faulty_index = index
            faulty_number = number_at_index
            print(f"Found fault at #{faulty_index}: {faulty_number}")
            break
        index += 1

    # Part 2
    index = 0
    while index < termination_index:
        sub_sum = int(data[index])
        next_index = index + 1
        while next_index < termination_index and sub_sum < faulty_number:
            sub_sum += int(data[next_index])
            next_index += 1
        if sub_sum == faulty_number:
            subset = list(map(int, data[index:next_index]))
            low, high = min(subset), max(subset)
            print(f"Range found between #{index} and #{next_index}: {low} and {high} sum to to {low + high}")
            break
        index += 1
