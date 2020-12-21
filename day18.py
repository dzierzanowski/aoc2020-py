#!/usr/bin/env python3

def solve(exp):
    result = 0
    next_op = '+'  # The first number we encounter will be effectively added to zero
    next_num = None
    while exp:
        token = exp.pop(0)
        
        if token == '(':
            next_num = solve(exp)
        elif token == ')':
            break
        elif token in ['+', '*']:
            next_op = token
        else:
            next_num = int(token)

        if next_op and next_num:
            if next_op == '+':
                result += next_num
            if next_op == '*':
                result *= next_num
            next_op = None
            next_num = None

    return result

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    expressions = raw_data.split('\n')  # Make sure there's no newline at the end of data

    result = 0

    for expression in expressions:
        expression = expression.replace('(', ' ( ').replace(')', ' ) ').split()
        result += solve(expression)
    print(f"Result: {result}")
