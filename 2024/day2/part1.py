from functions import *


rows = []
for line in read_lines():
    rows.append(list(map(int, line.split())))

total = 0
for row in rows:
    if row == sorted(row) or row == sorted(row, reverse=True):  # check if row is in increasing or decreasing order
        if len(row) == len(set(row)):  # check if row has no duplicates
            valid = True
            for i in range(len(row) - 1):
                if abs(row[i] - row[i + 1]) > 3:
                    valid = False
                    break
            if valid:
                total += 1

print(total)  # 383
