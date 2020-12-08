#!/usr/bin/env python3
import string

def init_dict():
    return {
        'contains': {},
        'contained_by': set()
    }

# Recurrence! B)
def count_bags(bag_dict, bag_name):
    count = 1
    bag = bag_dict[bag_name]
    for inner_bag, inner_count in bag['contains'].items():
        print(f"{inner_count}")
        count += int(inner_count) * count_bags(bag_dict, inner_bag)
    return count

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n")  # Make sure there's no newline at the end of data

    bag_dict = {}

    for entry in data:
        entry = entry.rstrip('.')
        main_bag, inner_bags = entry.split(' contain ')

        main_bag = ' '.join(main_bag.split()[:2])

        if main_bag not in bag_dict:
            bag_dict[main_bag] = init_dict()

        inner_bags = inner_bags.split(', ')
        
        for bag in inner_bags:
            bag_split = bag.split()
            count = bag_split[0]
            if count == 'no':  # "no other bags", skip
                continue
            bag = ' '.join(bag_split[1:3])

            bag_dict[main_bag]['contains'][bag] = count
            if bag not in bag_dict:
                bag_dict[bag] = init_dict()
            bag_dict[bag]['contained_by'].add(main_bag)

    count = 0
    bags_containing = set()
    bags_to_check = ['shiny gold']
    while bags_to_check:
        bag = bags_to_check.pop()
        bags_to_check.extend(bag_dict[bag]['contained_by'])
        bags_containing.update(bag_dict[bag]['contained_by'])

    print(f"Bags which contain shiny gold: {len(bags_containing)}")

    print(f"Bags contained in shiny gold: {count_bags(bag_dict, 'shiny gold') - 1}")
