#!/usr/bin/env python3
import math, re

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n\n")

    mandatory_fields = [
        'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'
    ]
    height_exp = '^(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$'
    hair_exp = '^#[a-f0-9]{6}$'
    eye_cols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    passport_exp = '^\d{9}$'

    valid_count = len(data)
    print(f"Initial count: {valid_count}")

    for entry in data:
        fields = entry.split()
        entry_dict = dict([ field.split(':') for field in fields ])

        invalid = False

        for field in mandatory_fields:
            if field not in entry_dict:
                invalid = True
                break

        if not invalid and not (1920 <= int(entry_dict['byr']) <= 2002):
            print(f"Invalid byr: {entry_dict['byr']}")
            invalid = True

        if not invalid and not (2010 <= int(entry_dict['iyr']) <= 2020):
            print(f"Invalid iyr: {entry_dict['iyr']}")
            invalid = True

        if not invalid and not (2020 <= int(entry_dict['eyr']) <= 2030):
            print(f"Invalid eyr: {entry_dict['eyr']}")
            invalid = True

        if not invalid and not re.match(height_exp, entry_dict['hgt']):
            print(f"Invalid hgt: {entry_dict['hgt']}")
            invalid = True

        if not invalid and not re.match(hair_exp, entry_dict['hcl']):
            print(f"Invalid hcl: {entry_dict['hcl']}")
            invalid = True

        if not invalid and entry_dict['ecl'] not in eye_cols:
            print(f"Invalid ecl: {entry_dict['ecl']}")
            invalid = True

        if not invalid and not re.match(passport_exp, entry_dict['pid']):
            print(f"Invalid pid: {entry_dict['pid']}")
            invalid = True

        if invalid:  # Finally
            valid_count -= 1


    print(f"Valid count: {valid_count}")
