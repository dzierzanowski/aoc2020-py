#!/usr/bin/env python3
import math

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read().splitlines()

        width = len(raw_data[0])
        
        cases = [(1, False), (3, False), (5, False), (7, False), (1, True)]
        results = []

        for movement, skip_even in cases:
            print(f"{movement} {skip_even}")
            horizontal_pos = 0
            vertical_pos = -1
            tree_count = 0
            for row in raw_data:
                vertical_pos += 1
                if skip_even and vertical_pos % 2 == 1:
                    continue
                is_tree = row[horizontal_pos] == '#'
                if is_tree:
                    tree_count += 1
                horizontal_pos = (horizontal_pos + movement) % width
            results.append(tree_count)

        print(f"Results: {results} [{math.prod(results)}]")