#!/usr/bin/env python3
import string

def try_execution(data):
    index = 0
    visited_instructions = set()
    accumulator = 0
    broken = False

    termination_index = len(data)

    while True:
        if index in visited_instructions:
            print(f"Tried to repeat instruction {index}")
            broken = True
            break
        visited_instructions.add(index)
        line = data[index]
        inst, val = line.split()
        if inst == 'nop':
            index += 1
        if inst == 'acc':
            accumulator += int(val)
            index += 1
        if inst == 'jmp':
            index += int(val)
        if index == termination_index:
            break

    if not broken:
        print("This program looks fine!")

    print(f"Value of accumulator: {accumulator}")

    return not broken


if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data

    print("Plain data")
    try_execution(data)

    print()
    for i in range(0, len(data)):
        line = data[i]
        if line[:3] != 'acc':
            print(f"Trying to fix line {i + 1}")
            new_data = data[:]
            if line[:3] == 'nop':
                new_data[i] = 'jmp' + line[3:]
            else:
                new_data[i] = 'nop' + line[3:]
            is_successful = try_execution(new_data)
            if is_successful:
                break
