from functions import *


left_list = []
right_list = []

for line in read_lines():
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

total = 0
for count, number in enumerate(left_list):
    total += abs(number - right_list[count])

print(total)  # 2375403
