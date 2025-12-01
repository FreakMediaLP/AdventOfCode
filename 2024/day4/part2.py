from functions import *
import numpy as np


def apply_mask(mini_mask):  # replace cross-section letters with dots
    temp = mini_mask.copy()
    mask = np.array([["", ".", ""], [".", "", "."], ["", ".", ""]])
    temp[mask == "."] = "."
    return temp


lines = []
for line in read_lines():
    lines.append(list(line.strip()))

matrix = np.array(lines)
print(f"{matrix}\n")

variants = [
    np.array([["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]]),
    np.array([["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]]),
    np.array([["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]]),
    np.array([["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]])]

total = 0
for i in range(len(matrix) - 2):
    for j in range(len(matrix) - 2):
        fraction = matrix[i:i + 3, j:j + 3]  # create 3x3 matrix fraction
        fraction = apply_mask(fraction.copy())
        for variant in variants:
            if np.array_equal(fraction, variant):
                print(f"{fraction}\n")
                total += 1

print(total)  # 1850
