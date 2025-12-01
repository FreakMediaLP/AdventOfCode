from functions import *
import numpy as np


lines = []
for line in read_lines():
    lines.append(list(line.strip()))

matrix = np.array(lines)
print(f"{matrix}\n")


horizontal = []
for i in range(len(matrix)):
    line = ""
    column = matrix[i, :]
    for letter in column:
        line += letter
    horizontal.append(line)
print(f"horizontal: {horizontal}")


vertical = []
for i in range(len(matrix)):
    line = ""
    column = matrix[:, i]
    for letter in column:
        line += letter
    vertical.append(line)
print(f"vertical: {vertical}")


diagonal_left = []
for i in range(len(matrix)):
    lower_row = ""
    upper_row = ""
    for j in range(len(matrix) - i):
        lower_row += matrix[j + i, j]
        upper_row += matrix[j, j + i]
    diagonal_left.append(lower_row)
    diagonal_left.append(upper_row)
diagonal_left.pop(0)
print(f"diagonal_left: {diagonal_left}")


diagonal_right = []
for i in range(len(matrix)):
    lower_row = ""
    upper_row = ""
    for j in range(len(matrix) - i):
        lower_row += matrix[j + i, len(matrix) - 1 - j]
        upper_row += matrix[j, len(matrix) - 1 - j - i]
    diagonal_right.append(lower_row)
    diagonal_right.append(upper_row)
diagonal_right.pop(0)
print(f"diagonal_right: {diagonal_right}\n")

search_list = [horizontal, vertical, diagonal_left, diagonal_right]

total = 0
for letter_list in search_list:
    for row in letter_list:
        total += row.count("XMAS") + row.count("SAMX")

print(total)  # 2573
