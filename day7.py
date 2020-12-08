#!/usr/bin/env python3
import string

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")[:-1]

    for entry in data:
        entry = entry.rstrip('.')
        main_bag, bags = entry.split(' contain ')
