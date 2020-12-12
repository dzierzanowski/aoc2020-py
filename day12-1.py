#!/usr/bin/env python3

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

    orientation_to_direction = {
        0:   'E',
        90:  'S',
        180: 'W',
        270: 'N'
    }
    
    # Check what direction options we have
    # degrees = set()
    # for entry in data:
    #     if entry[0] in ['L', 'R']:
    #         degrees.add(entry[1:])
    # print(f"Possible degree values: {degrees}")

    ship_pos = {
        'y':   0,  # NS
        'x':   0,  # WE
        'rot': 0
    }

    for entry in data:
        cmd = entry[0]
        magnitude = int(entry[1:])
        if cmd in ['L', 'R']:
            sign = -1 if cmd == 'L' else 1
            new_rot = ship_pos['rot'] + magnitude * sign
            while new_rot < 0:
                new_rot += 360
            ship_pos['rot'] = new_rot % 360
        if cmd == 'F':
            # We simulate N/S/W/E based on direction
            cmd = orientation_to_direction[ship_pos['rot']]
        if cmd in ['N', 'S', 'W', 'E']:
            dx, dy = [ i * magnitude for i in movement_map[cmd]]
            # print(f"dx: {dx}, dy: {dy}")
            ship_pos['x'] += dx
            ship_pos['y'] += dy
    print(f"{ship_pos}")
    print(f"Manhattan distance: {abs(ship_pos['x']) + abs(ship_pos['y'])}")
