#!/usr/bin/env python3

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    rows = raw_data.split('\n')  # Make sure there's no newline at the end of data

    # cubes = {}
    cubes = set()

    for i, row in enumerate(rows):
        for j, tile in enumerate(row):
            # cubes[(j, i, 0)] = tile == '#'  # True if #, False if .
            if tile == '#':
                cubes.add((j, i, 0))

    for _ in range(0, 6):
        # initial_cubes = set(cubes.keys())
        initial_cubes = cubes
        # print(f"Initial cubes: {initial_cubes}")
        evaluated_cubes = set()
        new_cubes = set()

        for cube in initial_cubes:
            x, y, z = cube
            for nx in range(x - 1, x + 2):
                for ny in range(y - 1, y + 2):
                    for nz in range(z - 1, z + 2):
                        evaluated_cubes.add((nx, ny, nz))

        for cube in evaluated_cubes:
            x, y, z = cube
            active_neighbors = 0
            for nx in range(x - 1, x + 2):
                for ny in range(y - 1, y + 2):
                    for nz in range(z - 1, z + 2):
                        if (nx, ny, nz) in initial_cubes and (nx, ny, nz) != cube:
                            active_neighbors += 1
            if (cube in initial_cubes and 2 <= active_neighbors <= 3) or active_neighbors == 3:
                new_cubes.add(cube)
        cubes = new_cubes
    print(f"Result: {len(cubes)}")
