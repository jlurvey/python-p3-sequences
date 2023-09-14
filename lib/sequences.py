#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        f_list = []
    elif length == 1:
        f_list = [0]
    elif length > 1:
        f_list = [0, 1]

    while len(f_list) < length:
        next_number = f_list[-1] + f_list[-2]
        f_list.append(next_number)

    print(f_list)
