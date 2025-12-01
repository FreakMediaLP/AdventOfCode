from functions import *


left_list = []
right_list = []

for line in read_lines():
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

total = 0
for number in left_list:
    count = right_list.count(number)
    total += number * count

print(total)  # 23082277
