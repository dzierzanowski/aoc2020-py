#!/usr/bin/env python3

if __name__ == '__main__':
    data = [14, 8, 16, 0, 1, 17]
    limit = 30000000  # 2020 for part #1
    
    registry = {}
    for index, num in enumerate(data[:-1]):
        registry[num] = index
    
    epoch = len(data) - 1
    last_num = data[epoch]

    while epoch < (limit - 1):
        if last_num in registry:
            last_occurence = registry[last_num]
            delta = epoch - last_occurence
            registry[last_num] = epoch
            last_num = delta
        else:
            registry[last_num] = epoch
            last_num = 0
        epoch += 1

    print(f"Epoch {epoch}: {last_num}")
