#!/usr/bin/env python3
import copy

def sign(i):
    return int(i / abs(i))

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data
    data = [ list(row) for row in data ]  # Split to char arrays
    
    width = len(data[0])
    height = len(data)

    surroundings = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    tolerance = 5  # 4 for part #1

    iterations = 0
    state_changed = True
    while state_changed:
        iterations += 1
        state_changed = False
        new_data = copy.deepcopy(data)
        seats_taken = 0
        for h in range(0, height):
            for w in range(0, width):
                if data[h][w] == '.':  # Skip empty
                    continue
                neighbors = 0
                surroundings_current = copy.deepcopy(surroundings)
                for s in surroundings_current:
                    dh, dw = s
                    nh, nw = h + dh, w + dw
                    # print(f"nh: {nh}, nw: {nw}")
                    if not (0 <= nh < height) or not (0 <= nw < width):  # Skip out-of-bounds
                        continue
                    if data[nh][nw] == '#':  # If taken, count neighbor
                        neighbors += 1
                    if data[nh][nw] == '.':  # If floor, perform dark magic
                        surroundings_current.append(tuple([(abs(i) + 1) * sign(i) if i else 0 for i in s]))

                seat_taken = data[h][w] == '#'

                if not seat_taken and neighbors == 0:
                    new_data[h][w] = '#'
                    # print(f"Occupying seat ({h}, {w})")
                    state_changed = True
                if seat_taken and neighbors >= tolerance:
                    new_data[h][w] = 'L'
                    # print(f"Freeing seat ({h}, {w})")
                    state_changed = True

                
                if seat_taken:
                    seats_taken += 1
        data = new_data

        if not state_changed:
            print(f"No changes this iteration (#{iterations}), seats taken: {seats_taken}")
