#!/usr/bin/env python3
import string

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data
    data.append(0)  # Starting point
    data = sorted(list(map(int, data)))
    data.append(max(data) + 3)  # Ending point
    # print(f"{data}")

    count = {
        1: 0,
        2: 0,
        3: 0
    }

    for i in range(0, len(data) - 1):
        diff = data[i + 1] - data[i]
        count[diff] += 1
        # print(f"{data[i+1]} - {data[i]} = {diff}")

    print(f"Answer #1: {count[1] * count[3]}")

    # Part 2

    data.reverse()
    max_num = max(data)

    # Each entry represents possible combinations for each number
    count2 = {
        max_num: 1
    }

    for i in range(1, len(data)):
        num = data[i]
        combinations = 0
        for j in range(1, 4):
            candidate = num + j
            # print(f"Checking {num} + {j} = {candidate}")
            if candidate in data:
                # print(f"Found {candidate} in data")
                combinations += count2[candidate]
        count2[num] = combinations

    print(f"Possible combinations: {count2[0]}")
