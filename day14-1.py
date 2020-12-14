#!/usr/bin/env python3

class Mem(dict):
    def __init__(self, *args):
        dict.__init__(self, args)
        self._ones = 0
        self._zeros = 0
    def __setitem__(self, key, value):
        value = (value | self._ones) & self._zeros
        dict.__setitem__(self, key, value)
    def setmask(self, mask):
        self._ones = int(mask.replace('X', '0'), 2)  # We'll be ORing
        self._zeros = int(mask.replace('X', '1'), 2)  # We'll be ANDing

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data
    
    mem = Mem()
    
    for line in data:
        cmd, val = line.split(' = ')
        if cmd == 'mask':
            mem.setmask(val)
        else:
            exec(line)

    print(f"Sum: {sum(mem.values())}")
