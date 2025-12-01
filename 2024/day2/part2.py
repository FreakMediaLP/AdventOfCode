from functions import *


def is_valid(row):
    if row == sorted(row) or row == sorted(row, reverse=True):  # check if row is in increasing or decreasing order
        if len(row) == len(set(row)):  # check if row has no duplicates
            for i in range(len(row) - 1):
                if abs(row[i] - row[i + 1]) > 3:
                    return False
            return True
    return False


def validate_variants(row):
    for i in range(len(row)):
        modified_row = row[:i] + row[i + 1:]
        if is_valid(modified_row):
            return True
    return False


rows = []
for line in read_lines():
    rows.append(list(map(int, line.split())))

total_safe = 0
for row in rows:
    if is_valid(row) or validate_variants(row):
        total_safe += 1

print(total_safe)  # 436
