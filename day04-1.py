#!/usr/bin/env python3
import math

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n\n")
    mandatory_fields = [
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
    ]

    valid_count = len(data)
    print(f"Initial count: {valid_count}")

    for entry in data:
        for field in mandatory_fields:
            if field not in entry:
                valid_count -= 1
                break

    print(f"Valid count: {valid_count}")
