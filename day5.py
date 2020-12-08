#!/usr/bin/env python3
import re

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    raw_data = re.sub(r'[BR]', '1', raw_data)
    raw_data = re.sub(r'[FL]', '0', raw_data)
    data = raw_data.split("\n")[:-1]

    ids = set()
    
    for entry in data:
        row = int(entry[:7], base=2)
        col = int(entry[7:], base=2)
        ids.add(row * 8 + col)
    
    min_id = min(ids)
    max_id = max(ids)
    print(f"Max: {max_id}")

    all_ids = set(range(min_id, max_id))

    missing = all_ids - ids

    print(f"Missing IDs: {missing}")
