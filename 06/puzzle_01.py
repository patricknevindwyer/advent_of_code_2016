#!/usr/bin/python3

import collections
import sys


def read_code(filename):
    """
    Read a code and break it into lines
    """
    with open(filename, "r") as f:
        return f.read().split("\n")
        

def decode(lines):
    """
    column frequency reduction
    """
    decoded = []
    for idx in range(len(lines[0])):
        column_data = collect_column(lines, idx)
        car = collections.Counter(column_data).most_common(1)[0][0]
        decoded.append(car)
    return "".join(decoded)


def collect_column(lines, idx):
    cars = []
    for line in lines:
        cars.append(line[idx])
    return "".join(cars)


if __name__ == "__main__":
    filename = sys.argv[-1]
    data = read_code(filename)
    print(decode(data))