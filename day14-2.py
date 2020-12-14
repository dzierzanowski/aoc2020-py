#!/usr/bin/env python3
import itertools, numpy

class Mem(dict):
    def __init__(self, *args):
        dict.__init__(self, args)
        self._ones = 0
        self._zeros = 0
        self._offsets = []
    def __setitem__(self, key, value):
        key = (key | self._ones) & self._zeros
        for offset in self._offsets:
            dict.__setitem__(self, key + offset, value)
    def setmask(self, mask):
        self._ones = int(mask.replace('X', '0'), 2)  # We'll be ORing
        self._zeros = int(mask.replace('0', '1').replace('X', '0'), 2)  # We'll be ANDing
        offsets = []
        for index, elem in enumerate(reversed(mask)):
            if elem == 'X':
                offsets.append(2 ** index)
        combos = [ 0 ]
        for i in range(1, len(offsets) + 1):
            combos.extend(map(sum, itertools.combinations(offsets, i)))
        self._offsets = combos
        # print(f"Combos: {sorted(combos)}")


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
