#!/usr/bin/env python3

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    rules, my_ticket, other_tickets = raw_data.split('\n\n')  # Make sure there's no newline at the end of data
    rules = rules.split('\n')
    my_ticket = my_ticket.split('\n')[1]
    other_tickets = other_tickets.split('\n')[1:]

    rule_dict = {}
    rule_count = len(rules)

    for rule in rules:
        name, ranges = rule.split(': ')
        range1, range2 = ranges.split(' or ')
        range1_min, range1_max = list(map(int, range1.split('-')))
        range2_min, range2_max = list(map(int, range2.split('-')))
        rule_dict[name] = {
            'range1': {
                'min': range1_min,
                'max': range1_max
            },
            'range2': {
                'min': range2_min,
                'max': range2_max
            },
            'possibilites': set(range(0, rule_count))
        }

    error_rate = 0
    valid_tickets = [my_ticket]

    for ticket in other_tickets:
        numbers = list(map(int, ticket.split(',')))
        is_valid_ticket = True
        for number in numbers:
            is_valid_number = False
            for rule in rule_dict.values():
                r1_min = rule['range1']['min']
                r1_max = rule['range1']['max']
                r2_min = rule['range2']['min']
                r2_max = rule['range2']['max']
                if r1_min <= number <= r1_max or r2_min <= number <= r2_max:
                    # print(f"Found valid: {number}")
                    is_valid_number = True
                    break
            if not is_valid_number:
                # print(f"Found invalid: {number}")
                error_rate += number
                is_valid_ticket = False
        if is_valid_ticket:
            valid_tickets.append(ticket)
    print(f"Error rate: {error_rate}")

    # Part #2

    for ticket in valid_tickets:
        fields = list(map(int, ticket.split(',')))
        for index, field in enumerate(fields):
            is_valid_number = False
            for rule in rule_dict.values():
                r1_min = rule['range1']['min']
                r1_max = rule['range1']['max']
                r2_min = rule['range2']['min']
                r2_max = rule['range2']['max']
                if not (r1_min <= field <= r1_max or r2_min <= field <= r2_max):
                    rule['possibilites'].discard(index)

    filtered_rules = {}

    while rule_dict:
        rule = [ rule for rule in rule_dict if len(rule_dict[rule]['possibilites']) == 1 ][0]
        index = rule_dict[rule]['possibilites'].pop()
        # print(f"{rule}: {index}")
        filtered_rules[rule] = index
        del rule_dict[rule]
        for r in rule_dict.values():
            r['possibilites'].discard(index)

    result = 1
    my_ticket = list(map(int, my_ticket.split(',')))

    for rule, index in filtered_rules.items():
        if rule.startswith('departure'):
            result *= my_ticket[index]

    print(f"Result: {result}")
