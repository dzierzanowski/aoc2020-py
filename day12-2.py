#!/usr/bin/env python3
import math

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data

    movement_map = {
        'N': (-1,  0),
        'S': ( 1,  0),
        'W': ( 0, -1),
        'E': ( 0,  1)
    }

    orientation_to_action = {
        90:  (True,   1, -1),  # (swap coords, flip sign y, flip sign x)
        180: (False, -1, -1),
        270: (True,  -1,  1)
    }

    waypoint_pos = {
        'y': -1,
        'x': 10,
    }

    ship_pos = {
        'y': 0,  # NS
        'x': 0  # WE
    }

    for entry in data:
        cmd = entry[0]
        magnitude = int(entry[1:])
        if cmd in ['L', 'R']:
            sign = -1 if cmd == 'L' else 1
            rot = magnitude * sign
            if rot < 0:
                rot += 360
            swap, sign_y, sign_x = orientation_to_action[rot]
            if swap:
                x = waypoint_pos['x']
                waypoint_pos['x'] = waypoint_pos['y']
                waypoint_pos['y'] = x
            waypoint_pos['y'] *= sign_y
            waypoint_pos['x'] *= sign_x
        if cmd in ['N', 'S', 'W', 'E']:
            dy, dx = [ i * magnitude for i in movement_map[cmd]]
            # print(f"dx: {dx}, dy: {dy}")
            waypoint_pos['y'] += dy
            waypoint_pos['x'] += dx
        if cmd == 'F':
            dy, dx = [i * magnitude for i in waypoint_pos.values()]
            print(f"Moving {dx} {dy}")
            ship_pos['y'] += dy
            ship_pos['x'] += dx
    print(f"{ship_pos}")
    print(f"Manhattan distance: {abs(ship_pos['x']) + abs(ship_pos['y'])}")
