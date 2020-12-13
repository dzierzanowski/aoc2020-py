#!/usr/bin/env python3

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data
    departure_time, ids = data
    
    departure_time = int(departure_time)
    ids = set(ids.split(','))
    ids.remove('x')
    ids = list(map(int, ids))

    nearest_bus = None
    wait_time = 0

    while not nearest_bus:
        for i in ids:
            if departure_time % i == 0:
                nearest_bus = i
                break
        if not nearest_bus:
            wait_time += 1
            departure_time += 1

    print(f"Found bus {nearest_bus} after {wait_time} minutes, answer: {nearest_bus * wait_time}")
