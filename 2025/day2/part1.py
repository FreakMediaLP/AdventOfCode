from functions import *

id_input = read().split(",")
id_ranges = []
id_sum = 0

def is_invalid_id(num):
    if len(num) % 2 == 1:
        return False
    else:
        left = num[:int((len(num) / 2))]
        right = num[int((len(num) / 2)):]

        if left == right:
            print(num)
            return True


for each in id_input:
    id_ranges.append([int(each.split("-")[0]), int(each.split("-")[1]) + 1])

for each in id_ranges:
    for i in range(each[0], each[1]):
        if is_invalid_id(str(i)):
            id_sum += i

print(id_sum)  # 19219508902