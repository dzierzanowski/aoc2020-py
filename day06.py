#!/usr/bin/env python3
import string

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        raw_data = file.read()

    data = raw_data.split("\n\n")

    count_any = 0
    count_all = 0

    print(string.ascii_lowercase)

    for group in data:
        entries = group.split('\n')
        group_questions_any = set()
        group_questions_all = set(string.ascii_lowercase)
        for entry in entries:
            if not entry:  # Protect against empty rows
                continue
            group_questions_any |= set(entry)
            group_questions_all &= set(entry)
        group_count_any = len(group_questions_any)
        group_count_all = len(group_questions_all)
        print(f"Group counts: {group_count_any} {group_count_all}")
        count_any += group_count_any
        count_all += group_count_all

    print(f"Total count (any): {count_any}")
    print(f"Total count (all): {count_all}")
