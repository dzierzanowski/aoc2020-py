#!/usr/bin/env python3
import numpy

def safecast(val, t):
    try:
        return t(val)
    except (ValueError, TypeError):
        return None

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data
    _, ids = data
    
    ids = [safecast(i, int) for i in ids.split(',')]

    lcm = ids.pop()  # Starting point
    next_remainder = 0
    current_timestamp = lcm
    target_timestamp = None

    while not target_timestamp:
        next_id = None
        while not next_id:
            next_id = ids.pop()
            next_remainder += 1
        next_id_adj = next_id  # Adjusted to fit remainder
        while next_remainder > next_id_adj:
            next_id_adj += next_id
        # print(f"TS: {current_timestamp}, LCM: {lcm}, TS/LCM: {current_timestamp/lcm}, next_id: {next_id}, remainder: {next_remainder}")
        while True:
            if current_timestamp % next_id_adj != next_remainder:
                current_timestamp += lcm
            else:
                break
        lcm = numpy.lcm(lcm, next_id)
        if not ids:
            # We've been looking at the timestamp of the last bus, so adjust
            # for the earliest bus. Also, we have to take the remainder of LCM
            # which is something I don't fully understand, but it still works
            # that way.
            target_timestamp = (current_timestamp - next_remainder) % lcm
    print(f"Found time: {target_timestamp}")
    print(f"Last LCM: {lcm}")
